__author__ = 'demattia'

from ROOT import TFile, TH1F, TCanvas, TLegend
import math


def draw(h1, h2, x_title, y_title):
    h1.Draw()
    h2.Draw("same")
    h1.GetXaxis().SetTitle(x_title)
    h1.GetXaxis().SetTitleOffset(1.3)
    h1.GetYaxis().SetTitle(y_title)
    h1.GetYaxis().SetTitleOffset(1.6)


def draw_superimposed(h1, h2, name, x_title, y_title="Entries"):
    if h1.GetMaximum() > h2.GetMaximum():
        draw(h1, h2, x_title, y_title)
    else:
        draw(h2, h1, x_title, y_title)
    h2.SetLineColor(2)
    l = TLegend(0.6,0.7,0.9,0.9)
    l.AddEntry(h1, name+"_{gen}")
    l.AddEntry(h2, name+"_{reco}")
    l.Draw("same")
    return l


def draw_and_fit(h, xTitle):
    h.Draw()
    h.Fit("gaus")
    print h.GetFunction("gaus").GetParameter(0)
    mean = h.GetFunction("gaus").GetParameter(1)
    mean_error = h.GetFunction("gaus").GetParError(1)
    dist = str(abs(int(math.log10(abs(mean_error))))+2)
    print "dist =", dist
    print ("{0:."+dist+"f}").format(mean) + " +/- " + ("{0:."+dist+"}").format(mean_error)
    print str(mean) + " +/- " + str(mean_error)
    print str(h.GetFunction("gaus").GetParameter(2)) + " +/- " + str(h.GetFunction("gaus").GetParError(2))

    h.GetXaxis().SetTitle(xTitle)
    h.GetXaxis().SetTitleOffset(1.3)
    h.GetYaxis().SetTitle("Entries")
    h.GetYaxis().SetTitleOffset(1.6)


def plot_histograms(input_file_name, charge, par, par_name, unit):
    input_file = TFile(input_file_name, "READ")
    h_gen = input_file.FindObjectAny("pars_"+charge+"_"+par)
    h_reco = input_file.FindObjectAny("EstimatedPar_"+charge+"_"+par)
    h_error = input_file.FindObjectAny("EstimatedParError_"+charge+"_"+par)
    h_relError = input_file.FindObjectAny("EstimatedParRelError_"+charge+"_"+par)
    c = TCanvas("c", "c", 800, 800)
    c.Divide(2, 2)
    c.cd(1)
    l_1 = draw_superimposed(h_gen, h_reco, par_name, par_name+" "+unit)
    c.cd(2)
    draw_and_fit(h_error, par_name+"_{gen} - "+par_name+"_{reco} "+unit)
    c.cd(3)
    draw_and_fit(h_relError, "("+par_name+"_{gen} - "+par_name+"_{reco})/"+par_name+"_{gen}")
    return c, l_1, h_gen, h_reco, h_error, h_relError, input_file
