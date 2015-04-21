import math
import ROOT
# import sys
from DataFormats.FWLite import Events, Handle

events = Events(
    [
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_95_7_e21.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_100_7_tNV.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_101_7_3cX.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_102_8_6AL.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_103_8_lDP.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_104_7_Nfz.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_105_8_lNt.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_106_7_Lbf.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_107_7_pZV.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_108_8_QUM.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_109_7_0WS.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_10_7_EHy.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_110_7_S7Q.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_111_6_gcH.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_112_7_nNz.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_113_8_DFG.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_114_8_OIc.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_115_7_wOa.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_116_8_psP.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_117_7_SCf.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_118_7_bHv.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_119_8_bEp.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_11_1_pbQ.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_120_7_fXe.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_121_8_Klj.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_122_1_P9q.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_123_7_vYy.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_124_8_uju.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_125_7_vM7.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_126_8_xUR.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_127_7_3ME.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_128_8_WAb.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_129_7_XhF.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_12_7_hCE.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_130_7_kKJ.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_131_1_Ftu.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_13_7_z34.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_14_7_mhZ.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_15_7_ACa.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_16_1_bDK.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_17_7_V2w.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_18_7_jLG.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_19_7_3kM.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_1_7_hlO.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_20_1_411.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_21_7_Asd.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_22_7_UdA.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_23_7_atZ.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_24_7_CNS.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_25_8_bSU.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_26_1_e1F.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_27_8_A9l.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_28_7_4N9.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_29_8_6Zd.root',
    'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/MCProduction/demattia/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/HTo2LongLivedTo4F_MH_1000_MFF_350_CTau350To35000_8TeV_pythia6_v4_Summer12_DR53X_PU_S10_START53_V7C-v1_2_7_taB.root'
    ]
)

# create handle outside of loop
handle = Handle('std::vector<reco::Track>')
handleGen = Handle ('std::vector<reco::GenParticle>')
handleTracks = Handle('std::vector<reco::Track>')
handleSA = Handle('std::vector<reco::Track>')
handleTrigger = Handle('edm::TriggerResults')

# a label is just a tuple of strings that is initialized just like an edm::InputTag
label = ("hltL2Muons")
labelGen = ("genParticles")
labelTracks = ("refittedStandAloneMuons")
labelSA = ("standAloneMuons")
labelTrigger = ("TriggerResults")

# Disable drawing to the screen
# ROOT.gROOT.SetBatch() # don't pop up canvases

# Create histograms, etc.
ROOT.gROOT.SetStyle('Plain') # white background
# Note that the genParticle distances are in mm

outputFile = ROOT.TFile("TriggerEfficiencyPlots.root", "RECREATE")
outputFile.cd()

muonPtLowHist = ROOT.TH1F("MuonPtLow", "lowest pt of the two muons", 300, 0, 300)
muonPtLowHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
muonPtHighHist = ROOT.TH1F("MuonPtHigh", "highest pt of the two muons", 300, 0, 300)
muonPtHighHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
muons3DAngleHist = ROOT.TH1F("Muons3DAngle", "3D angle between the two muons", 100, -3.15, 3.15)
muons3DAngleHist.GetXaxis().SetTitle("3D angle")
offlinePtLowHist = ROOT.TH1F("OfflinePtLow", "lowest pt of the two RSA muons", 300, 0, 300)
offlinePtLowHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
offlinePtHighHist = ROOT.TH1F("OfflinePtHigh", "highest pt of the two RSA muons", 300, 0, 300)
offlinePtHighHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
SAPtLowHist = ROOT.TH1F("SAPtLow", "lowest pt of the two SA muons", 300, 0, 300)
SAPtLowHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
SAPtHighHist = ROOT.TH1F("SAPtHigh", "highest pt of the two SA muons", 300, 0, 300)
SAPtHighHist.GetXaxis().SetTitle("p_{T} [GeV/c]")
genPtLowHist = ROOT.TH1F("genPtLow", "genPtLow", 300, 0, 300)
genPtHighHist = ROOT.TH1F("genPtHigh", "genPtHigh", 300, 0, 300)
genLxyHist = ROOT.TH1F("genLxy", "genLxy", 100, 0, 400)
genLxyAndPtHist = ROOT.TH2F("genLxyAndPt", "genLxy and low muon Pt", 50, 0, 400, 60, 0, 300)
genLxyAndD0Hist = ROOT.TH2F("genLxyAndD0", "genLxy and low Pt muon d0", 50, 0, 400, 100, 0, 100)
genLxyAndGenPtHist = ROOT.TH2F("genLxyAndGenPt", "genLxy and low muon genPt", 50, 0, 400, 60, 0, 300)
genLxyAndOfflinePtHist = ROOT.TH2F("genLxyAndOfflinePt", "genLxy and low RSA muon Pt", 50, 0, 400, 60, 0, 300)
genLxyAndOfflineD0Hist = ROOT.TH2F("genLxyAndOfflineD0", "genLxy and low Pt RSA muon d0", 50, 0, 400, 100, 0, 100)
genLxyAndSAPtHist = ROOT.TH2F("genLxyAndSAPt", "genLxy and low SA muon Pt", 50, 0, 400, 60, 0, 300)
genLxyAndSAD0Hist = ROOT.TH2F("genLxyAndSAD0", "genLxy and low Pt SA muon d0", 50, 0, 400, 100, 0, 100)
genLxyTriggeredHist = ROOT.TH1F("TriggerVsLxy", "genLxy for triggered events", 100, 0, 400)
genLxyAndPtTriggeredHist = ROOT.TH2F("genLxyAndPtTriggered", "genLxy and low muon Pt for triggered events", 50, 0, 400, 60, 0, 300)
genLxyAndD0TriggeredHist = ROOT.TH2F("genLxyAndD0Triggered", "genLxy and low Pt muon d0 for triggered events", 50, 0, 400, 100, 0, 100)
genLxyAndGenPtTriggeredHist = ROOT.TH2F("genLxyAndGenPtTriggered", "genLxy and low muon genPt for triggered events", 50, 0, 400, 60, 0, 300)
genLxyAndOfflinePtTriggeredHist = ROOT.TH2F("genLxyAndOfflinePtTriggered", "genLxy and low RSA muon Pt for triggered events", 50, 0, 400, 60, 0, 300)
genLxyAndOfflineD0TriggeredHist = ROOT.TH2F("genLxyAndOfflineD0Triggered", "genLxy and low Pt RSA muon d0 for triggered events", 50, 0, 400, 100, 0, 100)
genLxyAndSAPtTriggeredHist = ROOT.TH2F("genLxyAndSAPtTriggered", "genLxy and low SA muon Pt for triggered events", 50, 0, 400, 60, 0, 300)
genLxyAndSAD0TriggeredHist = ROOT.TH2F("genLxyAndSAD0Triggered", "genLxy and low Pt SA muon d0 for triggered events", 50, 0, 400, 100, 0, 100)
# Lxy 0 to 50 cm
muonPtLowHist_Lxy_0_50 = ROOT.TH1F("MuonPtLow_Lxy_0_50", "lowest pt of the two muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
muonPtHighHist_Lxy_0_50 = ROOT.TH1F("MuonPtHigh_Lxy_0_50", "highest pt of the two muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
offlinePtLowHist_Lxy_0_50 = ROOT.TH1F("OfflinePtLow_Lxy_0_50", "lowest pt of the two RSA muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
offlinePtHighHist_Lxy_0_50 = ROOT.TH1F("OfflinePtHigh_Lxy_0_50", "highest pt of the two RSA muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
SAPtLowHist_Lxy_0_50 = ROOT.TH1F("SAPtLow_Lxy_0_50", "lowest pt of the two SA muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
SAPtHighHist_Lxy_0_50 = ROOT.TH1F("SAPtHigh_Lxy_0_50", "highest pt of the two SA muons for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
genPtLowHist_Lxy_0_50 = ROOT.TH1F("genPtLow_Lxy_0_50", "genPtLow for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
genPtHighHist_Lxy_0_50 = ROOT.TH1F("genPtHigh_Lxy_0_50", "genPtHigh for 0 < |L_{xy}| < 50 cm", 300, 0, 300)
# Lxy 50 to 100 cm
muonPtLowHist_Lxy_50_100 = ROOT.TH1F("MuonPtLow_Lxy_50_100", "lowest pt of the two muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
muonPtHighHist_Lxy_50_100 = ROOT.TH1F("MuonPtHigh_Lxy_50_100", "highest pt of the two muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
offlinePtLowHist_Lxy_50_100 = ROOT.TH1F("OfflinePtLow_Lxy_50_100", "lowest pt of the two RSA muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
offlinePtHighHist_Lxy_50_100 = ROOT.TH1F("OfflinePtHigh_Lxy_50_100", "highest pt of the two RSA muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
SAPtLowHist_Lxy_50_100 = ROOT.TH1F("SAPtLow_Lxy_50_100", "lowest pt of the two SA muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
SAPtHighHist_Lxy_50_100 = ROOT.TH1F("SAPtHigh_Lxy_50_100", "highest pt of the two SA muons for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
genPtLowHist_Lxy_50_100 = ROOT.TH1F("genPtLow_Lxy_50_100", "genPtLow for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
genPtHighHist_Lxy_50_100 = ROOT.TH1F("genPtHigh_Lxy_50_100", "genPtHigh for 50 < |L_{xy}| < 100 cm", 300, 0, 300)
# Lxy 100 to 200 cm
muonPtLowHist_Lxy_100_200 = ROOT.TH1F("MuonPtLow_Lxy_100_200", "lowest pt of the two muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
muonPtHighHist_Lxy_100_200 = ROOT.TH1F("MuonPtHigh_Lxy_100_200", "highest pt of the two muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
offlinePtLowHist_Lxy_100_200 = ROOT.TH1F("OfflinePtLow_Lxy_100_200", "lowest pt of the two RSA muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
offlinePtHighHist_Lxy_100_200 = ROOT.TH1F("OfflinePtHigh_Lxy_100_200", "highest pt of the two RSA muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
SAPtLowHist_Lxy_100_200 = ROOT.TH1F("SAPtLow_Lxy_100_200", "lowest pt of the two SA muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
SAPtHighHist_Lxy_100_200 = ROOT.TH1F("SAPtHigh_Lxy_100_200", "highest pt of the two SA muons for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
genPtLowHist_Lxy_100_200 = ROOT.TH1F("genPtLow_Lxy_100_200", "genPtLow for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
genPtHighHist_Lxy_100_200 = ROOT.TH1F("genPtHigh_Lxy_100_200", "genPtHigh for 100 < |L_{xy}| < 200 cm", 300, 0, 300)
# Lxy > 200 cm
muonPtLowHist_Lxy_200 = ROOT.TH1F("MuonPtLow_Lxy_200", "lowest pt of the two muons for |L_{xy}| < 200 cm", 300, 0, 300)
muonPtHighHist_Lxy_200 = ROOT.TH1F("MuonPtHigh_Lxy_200", "highest pt of the two muons for |L_{xy}| < 200 cm", 300, 0, 300)
offlinePtLowHist_Lxy_200 = ROOT.TH1F("OfflinePtLow_Lxy_200", "lowest pt of the two RSA muons for |L_{xy}| < 200 cm", 300, 0, 300)
offlinePtHighHist_Lxy_200 = ROOT.TH1F("OfflinePtHigh_Lxy_200", "highest pt of the two RSA muons for |L_{xy}| < 200 cm", 300, 0, 300)
SAPtLowHist_Lxy_200 = ROOT.TH1F("SAPtLow_Lxy_200", "lowest pt of the two SA muons for |L_{xy}| < 200 cm", 300, 0, 300)
SAPtHighHist_Lxy_200 = ROOT.TH1F("SAPtHigh_Lxy_200", "highest pt of the two SA muons for |L_{xy}| < 200 cm", 300, 0, 300)
genPtLowHist_Lxy_200 = ROOT.TH1F("genPtLow_Lxy_200", "genPtLow for |L_{xy}| < 200 cm", 300, 0, 300)
genPtHighHist_Lxy_200 = ROOT.TH1F("genPtHigh_Lxy_200", "genPtHigh for |L_{xy}| < 200 cm", 300, 0, 300)

passTrigger = 0
passL2Muons = 0
passOfflinePtCuts = 0
totalEvents = 0

eventNum = 0
totalEventNum = events.size()
# loop over events
for event in events:
    eventNum += 1
    try:
        # Note that there are also triggerResults for SIM and RECO which are not needed here. Take the HLT results.
        # If not specified it will take the last one by default which is the RECO.
        event.getByLabel(labelTrigger, "", "HLT", handleTrigger)
        triggerResults = handleTrigger.product()
        # print "number of paths = ", triggerResults.size()
    except:
        print "trigger results error"
        continue
    try:
        event.getByLabel(label, handle)
        muons = handle.product()
        event.getByLabel(labelTracks, handleTracks)
        tracks = handleTracks.product()
        event.getByLabel(labelSA, handleSA)
        SAs = handleSA.product()
        event.getByLabel(labelGen, handleGen)
        genParticles = handleGen.product()
    except:
        # print "No hlt muon found"
        continue

    if eventNum % (totalEventNum/100) == 0:
        print "Analyzed", str(eventNum/(totalEventNum/100))+"% of the events"
    # print "Analyzing event", eventNum

    muonsArray = []
    for muon in muons:
        if muon.hitPattern().dtStationsWithAnyHits() + muon.hitPattern().cscStationsWithAnyHits() > 1:
            muonsArray.append(muon)
    muonsArray = sorted(muonsArray, key=lambda mu: mu.pt(), reverse=True)

    tracksArray = []
    for track in tracks:
        if track.hitPattern().dtStationsWithValidHits() + track.hitPattern().cscStationsWithValidHits() > 1:
            tracksArray.append(track)
    tracksArray = sorted(tracksArray, key=lambda tk: tk.pt(), reverse=True)

    SAArray = []
    for SA in SAs:
        if SA.hitPattern().dtStationsWithValidHits() + SA.hitPattern().cscStationsWithValidHits() > 1:
            SAArray.append(SA)
    SAArray = sorted(SAArray, key=lambda tk: tk.pt(), reverse=True)

    transverseDecayLength = -1
    minGenPt = -1
    maxGenPt = -1
    for genParticle in genParticles:
        if abs(genParticle.pdgId()) == 13 and abs(genParticle.mother().pdgId()) == 13:
            if abs(genParticle.mother().mother().pdgId()) == 6002113:
                tempLxy = math.sqrt((genParticle.mother().vertex().x() - genParticle.vertex().x())**2 +
                                    (genParticle.mother().vertex().y() - genParticle.vertex().y())**2)
                # Skip events with two sensitive decays for simplicity
                if transverseDecayLength != -1 and transverseDecayLength != tempLxy:
                    continue
                if minGenPt == -1:
                    minGenPt = genParticle.pt()
                else:
                    minGenPt = min(minGenPt, genParticle.pt())
                if maxGenPt == -1:
                    maxGenPt = genParticle.pt()
                else:
                    maxGenPt = max(maxGenPt, genParticle.pt())
                transverseDecayLength = tempLxy
                # print transverseDecayLength
    # Only consider events with decays to muons
    if transverseDecayLength == -1:
        continue

    totalEvents += 1

    genLxyHist.Fill(transverseDecayLength)
    genPtLowHist.Fill(minGenPt)
    genPtHighHist.Fill(maxGenPt)
    if transverseDecayLength > 0:
        if transverseDecayLength < 50:
            genPtHighHist_Lxy_0_50.Fill(maxGenPt)
            genPtLowHist_Lxy_0_50.Fill(minGenPt)
        elif transverseDecayLength < 100:
            genPtHighHist_Lxy_50_100.Fill(maxGenPt)
            genPtLowHist_Lxy_50_100.Fill(minGenPt)
        elif transverseDecayLength < 200:
            genPtHighHist_Lxy_100_200.Fill(maxGenPt)
            genPtLowHist_Lxy_100_200.Fill(minGenPt)
        else:
            genPtHighHist_Lxy_200.Fill(maxGenPt)
            genPtLowHist_Lxy_200.Fill(minGenPt)

    genLxyAndGenPtHist.Fill(transverseDecayLength, minGenPt)
    if len(tracksArray) > 1:
        offlinePtLowHist.Fill(tracksArray[1].pt())
        offlinePtHighHist.Fill(tracksArray[0].pt())
        if transverseDecayLength > 0:
            if transverseDecayLength < 50:
                offlinePtHighHist_Lxy_0_50.Fill(tracksArray[0].pt())
                offlinePtLowHist_Lxy_0_50.Fill(tracksArray[1].pt())
            elif transverseDecayLength < 100:
                offlinePtHighHist_Lxy_50_100.Fill(tracksArray[0].pt())
                offlinePtLowHist_Lxy_50_100.Fill(tracksArray[1].pt())
            elif transverseDecayLength < 200:
                offlinePtHighHist_Lxy_100_200.Fill(tracksArray[0].pt())
                offlinePtLowHist_Lxy_100_200.Fill(tracksArray[1].pt())
            else:
                offlinePtHighHist_Lxy_200.Fill(tracksArray[0].pt())
                offlinePtLowHist_Lxy_200.Fill(tracksArray[1].pt())
        genLxyAndOfflinePtHist.Fill(transverseDecayLength, tracksArray[1].pt())
        genLxyAndOfflineD0Hist.Fill(transverseDecayLength, tracksArray[1].d0())
    if len(SAArray) > 1:
        SAPtLowHist.Fill(SAArray[1].pt())
        SAPtHighHist.Fill(SAArray[0].pt())
        if transverseDecayLength > 0:
            if transverseDecayLength < 50:
                SAPtHighHist_Lxy_0_50.Fill(SAArray[0].pt())
                SAPtLowHist_Lxy_0_50.Fill(SAArray[1].pt())
            elif transverseDecayLength < 100:
                SAPtHighHist_Lxy_50_100.Fill(SAArray[0].pt())
                SAPtLowHist_Lxy_50_100.Fill(SAArray[1].pt())
            elif transverseDecayLength < 200:
                SAPtHighHist_Lxy_100_200.Fill(SAArray[0].pt())
                SAPtLowHist_Lxy_100_200.Fill(SAArray[1].pt())
            else:
                SAPtHighHist_Lxy_200.Fill(SAArray[0].pt())
                SAPtLowHist_Lxy_200.Fill(SAArray[1].pt())
        genLxyAndSAPtHist.Fill(transverseDecayLength, SAArray[1].pt())
        genLxyAndSAD0Hist.Fill(transverseDecayLength, SAArray[1].d0())
    if len(muonsArray) > 1:
        genLxyAndPtHist.Fill(transverseDecayLength, muonsArray[1].pt())
        genLxyAndD0Hist.Fill(transverseDecayLength, muonsArray[1].d0())

    # if ptLow > 23 and ptHigh > 23 and angle < 2.5 and validChambersOne > 1 and validChambersTwo > 1:
    # Old trigger is 147 (no chambers and angle requirement). New trigger is 148.
    # if triggerResults.accept(147):
    if triggerResults.accept(148):
        passTrigger += 1
        genLxyTriggeredHist.Fill(transverseDecayLength)
        genLxyAndGenPtTriggeredHist.Fill(transverseDecayLength, minGenPt)
        if len(tracksArray) > 1:
            genLxyAndOfflinePtTriggeredHist.Fill(transverseDecayLength, tracksArray[1].pt())
            genLxyAndOfflineD0TriggeredHist.Fill(transverseDecayLength, tracksArray[1].d0())
        if len(SAArray) > 1:
            genLxyAndSAPtTriggeredHist.Fill(transverseDecayLength, SAArray[1].pt())
            genLxyAndSAD0TriggeredHist.Fill(transverseDecayLength, SAArray[1].d0())
        if len(muonsArray) > 1:
            genLxyAndPtTriggeredHist.Fill(transverseDecayLength, muonsArray[1].pt())
            genLxyAndD0TriggeredHist.Fill(transverseDecayLength, muonsArray[1].d0())
        if len(tracksArray) > 1 and min(tracksArray[0].pt(), tracksArray[1].pt()) > 26:
            passOfflinePtCuts += 1

    if len(muonsArray) < 2:
        # print "Less than 2 hlt muons found"
        continue

    muonPtHighHist.Fill(muonsArray[0].pt())
    muonPtLowHist.Fill(muonsArray[1].pt())
    if transverseDecayLength > 0:
        if transverseDecayLength < 50:
            muonPtHighHist_Lxy_0_50.Fill(muonsArray[0].pt())
            muonPtLowHist_Lxy_0_50.Fill(muonsArray[1].pt())
        elif transverseDecayLength < 100:
            muonPtHighHist_Lxy_50_100.Fill(muonsArray[0].pt())
            muonPtLowHist_Lxy_50_100.Fill(muonsArray[1].pt())
        elif transverseDecayLength < 200:
            muonPtHighHist_Lxy_100_200.Fill(muonsArray[0].pt())
            muonPtLowHist_Lxy_100_200.Fill(muonsArray[1].pt())
        else:
            muonPtHighHist_Lxy_200.Fill(muonsArray[0].pt())
            muonPtLowHist_Lxy_200.Fill(muonsArray[1].pt())
    angle = math.acos((muonsArray[0].px()*muonsArray[1].px() +
                       muonsArray[0].py()*muonsArray[1].py() +
                       muonsArray[0].pz()*muonsArray[1].pz())/(muonsArray[0].p()*muonsArray[1].p()))
    muons3DAngleHist.Fill(angle)
    validChambersOne = muonsArray[0].hitPattern().dtStationsWithAnyHits() + muonsArray[0].hitPattern().cscStationsWithAnyHits()
    validChambersTwo = muonsArray[1].hitPattern().dtStationsWithAnyHits() + muonsArray[1].hitPattern().cscStationsWithAnyHits()

    # if triggerResults.accept(147) and muonsArray[1].pt() > 23:
    if triggerResults.accept(147) and angle <= 2.5 and validChambersOne > 1 and validChambersTwo > 1:
        passL2Muons += 1

triggerEfficiency = passTrigger/float(totalEvents)
triggerEfficiencyError = math.sqrt(triggerEfficiency*(1-triggerEfficiency)/totalEvents)
print "trigger efficiency from triggerResults =", triggerEfficiency, "+/-", triggerEfficiencyError

# triggerEfficiencyL2Muons = passL2Muons/float(totalEvents)
# triggerEfficiencyL2MuonsError = math.sqrt(triggerEfficiencyL2Muons*(1-triggerEfficiencyL2Muons)/totalEvents)
# print "trigger efficiency from L2Muons =", triggerEfficiencyL2Muons, "+/-", triggerEfficiencyL2MuonsError

passOfflinePtCutsEfficiency = passOfflinePtCuts/float(totalEvents)
passOfflinePtCutsEfficiencyError = math.sqrt(passOfflinePtCutsEfficiency*(1-passOfflinePtCutsEfficiency)/totalEvents)
print "offline pt cuts efficiency =", passOfflinePtCutsEfficiency, "+/-", passOfflinePtCutsEfficiencyError

# make a canvas, draw, and save it
c1 = ROOT.TCanvas("c1", "c1", 800, 1600)
c1.Divide(2, 4)
c1.cd(1)
muonPtLowHist.Draw()
lineLow = ROOT.TLine(23, 0, 23, muonPtLowHist.GetMaximum())
lineLow.SetLineColor(2)
lineLow.SetLineWidth(2)
lineLow.Draw()
c1.cd(2)
muonPtHighHist.Draw()
lineHigh = ROOT.TLine(23, 0, 23, muonPtHighHist.GetMaximum())
lineHigh.SetLineColor(2)
lineHigh.SetLineWidth(2)
lineHigh.Draw()
c1.cd(3)
offlinePtLowHist.Draw()
offlineLineLow = ROOT.TLine(23, 0, 23, offlinePtLowHist.GetMaximum())
offlineLineLow.SetLineColor(2)
offlineLineLow.SetLineWidth(2)
offlineLineLow.Draw()
c1.cd(4)
offlinePtHighHist.Draw()
offlineLineHigh = ROOT.TLine(23, 0, 23, offlinePtHighHist.GetMaximum())
offlineLineHigh.SetLineColor(2)
offlineLineHigh.SetLineWidth(2)
offlineLineHigh.Draw()
c1.cd(3)
offlinePtLowHist.Draw()
offlineLineLow = ROOT.TLine(23, 0, 23, offlinePtLowHist.GetMaximum())
offlineLineLow.SetLineColor(2)
offlineLineLow.SetLineWidth(2)
offlineLineLow.Draw()
c1.cd(4)
offlinePtHighHist.Draw()
offlineLineHigh = ROOT.TLine(23, 0, 23, offlinePtHighHist.GetMaximum())
offlineLineHigh.SetLineColor(2)
offlineLineHigh.SetLineWidth(2)
offlineLineHigh.Draw()
c1.cd(5)
SAPtLowHist.Draw()
SALineLow = ROOT.TLine(23, 0, 23, SAPtLowHist.GetMaximum())
SALineLow.SetLineColor(2)
SALineLow.SetLineWidth(2)
SALineLow.Draw()
c1.cd(6)
SAPtHighHist.Draw()
SALineHigh = ROOT.TLine(23, 0, 23, SAPtHighHist.GetMaximum())
SALineHigh.SetLineColor(2)
SALineHigh.SetLineWidth(2)
SALineHigh.Draw()
c1.cd(7)
# muons3DAngleHist.Draw()
# lineAngle = ROOT.TLine(2.5, 0, 2.5, muons3DAngleHist.GetMaximum())
# lineAngle.SetLineColor(2)
# lineAngle.SetLineWidth(2)
# lineAngle.Draw()
genPtLowHist.Draw()
genLineLow = ROOT.TLine(23, 0, 23, genPtLowHist.GetMaximum())
genLineLow.SetLineColor(2)
genLineLow.SetLineWidth(2)
genLineLow.Draw()
c1.cd(8)
genPtHighHist.Draw()
genLineHigh = ROOT.TLine(23, 0, 23, genPtHighHist.GetMaximum())
genLineHigh.SetLineColor(2)
genLineHigh.SetLineWidth(2)
genLineHigh.Draw()
c1.Print("L2Muons.png")

c2 = ROOT.TCanvas("c2", "c2", 800, 1200)
c2.Divide(2, 3)
c2.cd(1)
genLxyHist.Draw()
genLxyTriggeredHist.Draw("same")
genLxyTriggeredHist.SetLineColor(2)
c2.cd(2)
effVsGenLxy = ROOT.TEfficiency(genLxyTriggeredHist, genLxyHist)
effVsGenLxy.Draw()
c2.cd(3)
genLxyAndPtHist.Draw("COLZ")
c2.cd(4)
genLxyAndPtTriggeredHist.Draw("COLZ")
c2.cd(5)
genLxyAndGenPtHist.Draw("COLZ")
c2.cd(6)
genLxyAndGenPtTriggeredHist.Draw("COLZ")
c2.Print("TriggerVsLxy.png")

c3 = ROOT.TCanvas("c3", "c3", 800, 800)
c3.Divide(2, 2)
c3.cd(1)
genLxyAndOfflinePtHist.Draw("COLZ")
c3.cd(2)
genLxyAndOfflinePtTriggeredHist.Draw("COLZ")
c3.cd(3)
genLxyAndSAPtHist.Draw("COLZ")
c3.cd(4)
genLxyAndSAPtTriggeredHist.Draw("COLZ")
c3.Print("TriggerVsLxy_offline.png")

c4 = ROOT.TCanvas("c4", "c4", 800, 800)
c4.Divide(2, 2)
c4.cd(1)
genLxyAndD0Hist.Draw("COLZ")
c4.cd(2)
genLxyAndD0TriggeredHist.Draw("COLZ")
c4.cd(3)
genLxyAndOfflineD0Hist.Draw("COLZ")
c4.cd(4)
genLxyAndOfflineD0TriggeredHist.Draw("COLZ")
c4.Print("TriggerVsLxy_d0.png")

outputFile.Write()
