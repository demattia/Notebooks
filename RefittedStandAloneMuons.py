#import ROOT
# from utils import deltaR
import math
import ROOT

muMass = 0.1057

<<<<<<< HEAD

=======
>>>>>>> 906a95bcc56d3ed7061b2df61d04773443a33409
def computeCosineAndMass(mu1, mu2):
    muon1 = ROOT.TLorentzVector()
    muon2 = ROOT.TLorentzVector()
    muon1.SetPtEtaPhiM(mu1.pt, mu1.eta, mu1.phi, muMass)
    muon2.SetPtEtaPhiM(mu2.pt, mu2.eta, mu2.phi, muMass)
    cosine = math.cos(muon1.Angle(muon2.Vect()))
    mass = (muon1+muon2).M()
    return (cosine, mass)


def deltaPhi(phi1, phi2):
    result = phi1 - phi2;
    if result > math.pi: result -= 2*math.pi
    if result <= -math.pi: result += 2*math.pi
    return result


def deltaR(v1, v2):
    return math.sqrt(deltaPhi(v1.phi, v2.phi)**2 + (v1.eta-v2.eta)**2)


def is_matched_lepton(lepton, chosen_pdg_id, signal_pdg_ids):
    """
    Checks whether the reconstructed lepton is matched to a generated lepton coming from a given particle decay.
    It explicitly checks that the lepton is a standAloneMoun (which is a refittedStandAloneMuon in the current tree).
    """
    if lepton.isStandAloneMuon and abs(lepton.genPdgId) == chosen_pdg_id:
        for signalPdgId in signal_pdg_ids:
            if lepton.genSignalOriginPdgId == signalPdgId:
                return True
    return False


def decay_to_chosen_pdg_id(event, ll_idx, chosen_pdg_id):
    """
    Returns true if both leptons decay to the chosen pdgId.
    @param event:
    @param chosen_pdg_id:
    @return:
    """
    if (abs(getattr(event, ll_idx+"_daughter1_PdgId")) == chosen_pdg_id and
       abs(getattr(event, ll_idx+"_daughter2_PdgId")) == chosen_pdg_id):
        return True
    return False


def is_selected_signal(event, signal_pdg_ids):
    """
    Returns true if the event has long-lived particles of the selected signal type.
    We have different decay length samples in the same file.
    """
    selected_signal1 = False
    selected_signal2 = False
    for signal_pdg_id in signal_pdg_ids:
        if event.ll1_motherPdgId == signal_pdg_id:
            selected_signal1 = True
        if event.ll2_motherPdgId == signal_pdg_id:
            selected_signal2 = True
    if selected_signal1 is False or selected_signal2 is False:
        return False
    return True


def is_within_acceptance(event, ll_idx, pt_cut, eta_cut, lxy_cut):
    """
    Returns true if the given long-lived particle is in the acceptance.
    @param ll_idx: either ll1 or ll2. Used to get the corresponding long-lived particle in the event.
    """
    if getattr(event, ll_idx+"_decayLength2D") < lxy_cut:
        if (getattr(event, ll_idx+"_daughter1_Pt") > pt_cut and
           abs(getattr(event, ll_idx+"_daughter1_Eta")) < eta_cut and
           getattr(event, ll_idx+"_daughter2_Pt") > pt_cut and
           abs(getattr(event, ll_idx+"_daughter2_Eta")) < eta_cut):
            return True
    return False


def get_lepton(leptons, index):
    """
    Loop over TreeLeptons and get the ones corresponding to the indeces in this candidate.
    """
    for lepton in leptons:
        if lepton.index >= 0 and index == abs(lepton.index):
            return lepton
    print "Error: no matching lepton found."
    return


def pass_muon_cuts(lepton, pt_cut, eta_cut, chi2_cut, min_stations_with_valid_hits_cut):
    if (lepton.pt > pt_cut and abs(lepton.eta) < eta_cut and lepton.trackChi2 > chi2_cut and
       # lepton.triggerMatch != 0 and
       lepton.dtStationsWithValidHits+lepton.cscStationsWithValidHits >= min_stations_with_valid_hits_cut):
        return True
    return False


def signal_trigger_fired(triggers, signal_trigger):
    for trigger in triggers:
        if trigger == signal_trigger:
            return True
    return False


# def is_complementary(leptonL, leptonH, candidates):
def is_complementary(leptonL, leptonH, passing_candidates):
    """
    Complementarity requirement (reject candidates already selected by the track-based analysis).
    """
    min_deltaR_L = 100000
    min_deltaR_H = 100000
    # passing_candidates = passing_track_based_candidates(leptonL, leptonH, candidates)
    for passing_candidate in passing_candidates:
        track_lepton_L = passing_candidate[1]
        track_lepton_H = passing_candidate[2]
        # the threshold is 0.1, and we require deltaR > 0.2 between the two leptons so the
        # two L and H cannot be matched to the same track.
        deltaR_L = min(deltaR(leptonL, track_lepton_L), deltaR(leptonL, track_lepton_H))
        deltaR_H = min(deltaR(leptonH, track_lepton_L), deltaR(leptonH, track_lepton_H))
        if deltaR_L < min_deltaR_L: min_deltaR_L = deltaR_L
        if deltaR_H < min_deltaR_H: min_deltaR_H = deltaR_H
    # If the refittedStandAloneMuons candidate matches a track-based candidate passing the full selection
    if min_deltaR_L < 0.1 and min_deltaR_H < 0.1:
        return False
    return True


def fill_overflow(h, value):
    if h.FindBin(value) < h.GetNbinsX():
        h.Fill(value)
    else:
        h.Fill(h.GetBinCenter(h.GetNbinsX()))


def passing_track_based_candidates(candidates):
    """
    Return a list of track-based candidates passing the full track-based analysis selection.
    """
    passing_candidates = []
    for candidate in candidates.candidates_:
        track_lepton_L = get_lepton(candidates.leptons_, candidate.leptonIndexL)
        track_lepton_H = get_lepton(candidates.leptons_, candidate.leptonIndexH)
        if (track_lepton_L.isCentralTrack and track_lepton_H.isCentralTrack and
           track_lepton_L.pt > 26 and abs(track_lepton_L.eta) < 2. and track_lepton_L.iso/track_lepton_L.pt < 0.1 and
           track_lepton_H.pt > 26 and abs(track_lepton_H.eta) < 2. and track_lepton_H.iso/track_lepton_H.pt < 0.1 and
           candidate.hitsBeforeVertexL+candidate.hitsBeforeVertexH <= 1 and
           candidate.missedLayersAfterVertexL+candidate.missedLayersAfterVertexH <= 4 and
           candidate.deltaR > 0.2 and candidate.cosine > -0.79 and candidate.corrDileptonMass > 15. and
           track_lepton_L.charge*track_lepton_H.charge == -1 and candidate.vertexChi2 < 5 and
           track_lepton_L.triggerMatch != 0 and track_lepton_H.triggerMatch != 0 and candidate.differentTO and
           # candidate.dPhiCorr > 0. and candidate.dPhiCorr <= math.pi/2.):
           abs(candidate.leptonD0SignificanceL_PVrefit_includingPVError) > 12. and
           abs(candidate.leptonD0SignificanceH_PVrefit_includingPVError) > 12.):
            passing_candidates.append([candidate, track_lepton_L, track_lepton_H])
            # print "found a track-based candidate"
            # print "leptonL pt, eta, iso =", track_lepton_L.pt, track_lepton_L.eta, track_lepton_L.iso/track_lepton_L.pt
            # print "leptonL d0/sigma =", candidate.leptonD0SignificanceL_PVrefit_includingPVError
            # print "leptonH pt, eta, iso =", track_lepton_H.pt, track_lepton_H.eta, track_lepton_H.iso/track_lepton_H.pt
            # print "leptonH d0/sigma =", candidate.leptonD0SignificanceH_PVrefit_includingPVError
            # print "hitsBeforeVertex =", candidate.hitsBeforeVertexL+candidate.hitsBeforeVertexH
            # print "missedLayersAfterVertex =", candidate.missedLayersAfterVertexL+candidate.missedLayersAfterVertexH
            # print "deltaR, cosine, mass =", candidate.deltaR, candidate.cosine, candidate.corrDileptonMass
    return passing_candidates
