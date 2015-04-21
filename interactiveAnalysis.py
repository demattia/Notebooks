#!/usr/bin/env python

import sys
import os
import time
import random

import ROOT

def help():
    print "help()                                -- this message"
    print "print variables                       -- print a list of variables that can be used for plotting"
    print "cuts                                  -- show the current list of cuts"
    print "cuts.append(\"candidates_.mass < 10\")  -- add a cut to the list"
    print "del cuts[3]                           -- remove a cut from the list (etc... cuts acts like a list)"
    print "cuts.clear()                          -- forget all cuts"
    print "eventLimit = 10000                    -- limit the number of events plotted, to get quick feedback (10000 by default)"
    print "eventLimit = None                     -- do not limit the number of events"
    print "plot(\"dimu.mass\")                     -- plot a quantity with the current cuts and current eventLimit"
    print "plot(\"dimu.mass\", \"mu.pt > 30\")       -- plot a quantity with current cuts AND one more"
    print "cuts2 = cuts.copy()                   -- make another set of cuts"
    print "plot(\"dimu.mass\", cuts2)              -- plot a quantity with a different set of cuts"
    print "plot(\"dimu.mass\", overlay=ROOT.kRed)  -- overlay this plot on the previous one, in the specified color"
    print "h = getHistogram(\"histogram_iz6Xsb\")  -- access a previously saved histogram"
    print "h.Draw(\"e1\")                          -- redraw a histogram using ROOT options (\"e1\" in this case)"
    print "fit(h, \"A*exp(-(x-mu)**2/2/sigma)/sqrt(6.28)/sigma\", A=1000, mu=90, sigma=10)"
    print "                                      -- fit a histogram to a function (in this case, Gaussian)"

variables = """The most useful variables:

dimu.mass                             -- mass of dimuon candidate
dimu.pt                               -- transverse momentum of dimuon candidate
dimu.eta                              -- pseudorapidity of dimuon candidate
dimu.phi                              -- azimuthal direction of dimuon candidate
dimu.decayLength                      -- distance between primary and secondary vertex
dimu.decayLengthSignificance          -- decayLength divided by uncertainty in decayLength
dimu.vx                               -- secondary vertex position (x)
dimu.vy                               -- secondary vertex position (y)
dimu.vz                               -- secondary vertex position (z)
dimu.dPhi                             -- angle between dimuon momentum and primary -> secondary vertex displacement vector
dimu.hitsBeforeVertexH                -- number of hits on the high-pT muon track between the primary and secondary vertices
dimu.hitsBeforeVertexL                -- same for the low-pT muon track
dimu.missedLayersAfterVertexH         -- number of tracker layers without hits for the high-pT muon track
dimu.missedLayersAfterVertexL         -- same for the low-pT muon track

mu.pt                                 -- transverse momentum of each muon
mu.eta                                -- pseudorapidity of each muon
mu.phi                                -- azimuthal angle of each muon
mu.d0                                 -- impact parameter in the transverse plane for each muon
mu.absD0Significance                  -- d0 divided by uncertainty in d0
"""

# a class to keep track of cuts
class Cuts:
    def __init__(self):
        self._cuts = []
        
    # pretend Cuts is a list
    def __len__(self): return len(self._cuts)
    def __getitem__(self, key): return self._cuts[key]
    def __setitem__(self, key, value): self._cuts[key] = value
    def __delitem__(self, key): del self._cuts[key]
    def append(self, *args, **kwds): return self._cuts.append(*args, **kwds)
    def extend(self, *args, **kwds): return self._cuts.extend(*args, **kwds)
    def count(self, *args, **kwds): return self._cuts.count(*args, **kwds)
    def index(self, *args, **kwds): return self._cuts.index(*args, **kwds)
    def insert(self, *args, **kwds): return self._cuts.insert(*args, **kwds)
    def remove(self, *args, **kwds): return self._cuts.remove(*args, **kwds)
    def pop(self, *args, **kwds): return self._cuts.pop(*args, **kwds)
    def reverse(self, *args, **kwds): return self._cuts.reverse(*args, **kwds)
    def sort(self, *args, **kwds): return self._cuts.sort(*args, **kwds)

    # display cuts in a useful way
    def __repr__(self):
        if len(self._cuts) == 0:
            return "No cuts have been defined"
        output = ["Requiring all of the following:"]
        for i, c in enumerate(self._cuts):
            output.append("    cuts[%d] \"%s\"" % (i, c))
        return os.linesep.join(output)

    # give a cut string to ROOT
    def __str__(self):
        if len(self._cuts) == 0:
            return ""
        else:
            return "(" + ") && (".join(self._cuts) + ")"

    # copy this set of cuts
    def copy(self):
        output = Cuts()
        output._cuts = self._cuts[:]
        return output

    # forget all cuts
    def clear(self): self._cuts = []

# a class to predict how long it will take to plot something
class Timing:
    numerator = None
    denominator = None

    @classmethod
    def prediction(__class__, numEvents):
        if __class__.numerator is None:
            return ""
        else:
            return ", which should take %.2f minutes" % (__class__.numerator / __class__.denominator * numEvents)

    def __init__(self, numEvents):
        self.numEvents = numEvents

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.end = time.time()

        if self.__class__.numerator is None:
            self.__class__.numerator = 0.
            self.__class__.denominator = 0.

        self.__class__.numerator += (self.end - self.start)/60.
        self.__class__.denominator += self.numEvents


class InteractiveAnalysis:

    def randomName(self):
        return "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 10))

    # function to draw a plot
    def plot(self, quantity, extracuts=None, overlay=None, fillHistogram=None):
        print "Plotting \"%s\"" % quantity

        title = "\"%s\"" % quantity
        quantity = quantity.replace("dimu.", "candidates_.")
        quantity = quantity.replace("mu.", "leptons_.")

        if extracuts is None:
            cutstring = str(self.cuts)
            print repr(self.cuts)
        elif isinstance(extracuts, Cuts):
            cutstring = str(extracuts)
            print repr(extracuts)
        elif isinstance(extracuts, basestring):
            cutstring = str(self.cuts)

            if cutstring == "":
                cutstring = extracuts
                print "Cutting only \"%s\"" % extracuts
            else:
                cutstring += (" && (%s)" % extracuts)
                print repr(self.cuts)
                print "    and also \"%s\"" % extracuts

        if cutstring != "":
            title += " cut with \"%s\"" % cutstring
        cutstring = cutstring.replace("dimu.", "candidates_.")
        cutstring = cutstring.replace("mu.", "leptons_.")

        fillHistogram = "histogram_" + self.randomName()

        print "Using %d input events%s" % (self.eventLimit, Timing.prediction(self.eventLimit))
        with Timing(self.eventLimit):
            if self.eventLimit is None:
                numPass = self.ttree.Project(fillHistogram, quantity, cutstring)
            else:
                numPass = self.ttree.Project(fillHistogram, quantity, cutstring, "Q", self.eventLimit)

        if numPass == 0:
            print "No events passed the cuts."
        else:
            print "You should see %d events in the plot." % numPass

            output = ROOT.gROOT.FindObject(fillHistogram)
            output.SetTitle(title)
            if overlay is None:
                output.Draw()
            else:
                output.SetLineColor(overlay)
                output.Draw("same")

            return output

    def getHistogram(self, name):
        return ROOT.gROOT.FindObject(name)

    def fit(self, histogram, functionString, **initialValues):
        variableNames = initialValues.keys()
        for i, name in enumerate(variableNames):
            functionString = functionString.replace(name, "[%d]" % i)

        low = h.GetBinLowEdge(1)
        high = h.GetBinLowEdge(h.GetNbinsX()) + h.GetBinWidth(h.GetNbinsX())

        functionName = "function_" + self.randomName()
        function = ROOT.TF1(functionName, functionString, low, high)

        for i, name in enumerate(variableNames):
            function.SetParName(i, name)
            function.SetParameter(i, initialValues[name])

        histogram.Fit(function, "Q")

        parameters = {}
        parameters["chi2"] = histogram.GetFunction(functionName).GetChisquare()
        parameters["ndf"] = histogram.GetFunction(functionName).GetNDF()
        parameters["pvalue"] = ROOT.TMath.Prob(parameters["chi2"], parameters["ndf"])

        for i, name in enumerate(variableNames):
            parameters[name] = histogram.GetFunction(functionName).GetParameter(i)

        return parameters

    # where the execution starts
    def __init__(self, rootFileName):
        if not os.path.exists(rootFileName):
            sys.stderr.write("Incorrect root file argument \"%s\"." % rootFileName)
            sys.stderr.write(os.linesep)
            sys.exit(-1)

        self.rootFile = ROOT.TFile(rootFileName)
        self.ttree = self.rootFile.Get("muTrackAnalysis/outputTree")

        self.cuts = Cuts()
        self.eventLimit = 10000

        # help()
