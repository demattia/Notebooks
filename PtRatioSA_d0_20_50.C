{
//=========Macro generated from canvas: cRatio/cRatio
//=========  (Wed Oct 22 18:47:21 2014) by ROOT version5.34/18
   TCanvas *cRatio = new TCanvas("cRatio", "cRatio",0,0,400,400);
   gStyle->SetOptStat(0);
   cRatio->SetHighLightColor(2);
   cRatio->Range(0,0,1,1);
   cRatio->SetFillColor(0);
   cRatio->SetBorderMode(0);
   cRatio->SetBorderSize(2);
   cRatio->SetFrameBorderMode(0);
   
   TH1F *h1Ratio_Data = new TH1F("h1Ratio_Data","",25,0,100);
   h1Ratio_Data->SetBinContent(7,1.847327);
   h1Ratio_Data->SetBinContent(8,1.895273);
   h1Ratio_Data->SetBinContent(9,1.368892);
   h1Ratio_Data->SetBinContent(10,1.403174);
   h1Ratio_Data->SetBinContent(11,0.8639166);
   h1Ratio_Data->SetBinContent(12,0.7551621);
   h1Ratio_Data->SetBinContent(13,1.096439);
   h1Ratio_Data->SetBinContent(14,0.868835);
   h1Ratio_Data->SetBinContent(15,0.9066508);
   h1Ratio_Data->SetBinContent(16,1.015325);
   h1Ratio_Data->SetBinContent(17,0.8387465);
   h1Ratio_Data->SetBinContent(18,0.7039585);
   h1Ratio_Data->SetBinContent(19,1.020873);
   h1Ratio_Data->SetBinContent(20,0.8461039);
   h1Ratio_Data->SetBinContent(21,0.8022318);
   h1Ratio_Data->SetBinContent(22,0.5206793);
   h1Ratio_Data->SetBinContent(23,0.7445714);
   h1Ratio_Data->SetBinContent(24,0.3999764);
   h1Ratio_Data->SetBinContent(25,0.5415065);
   h1Ratio_Data->SetBinContent(26,0.813337);
   h1Ratio_Data->SetBinError(7,0.2481906);
   h1Ratio_Data->SetBinError(8,0.1903219);
   h1Ratio_Data->SetBinError(9,0.1442961);
   h1Ratio_Data->SetBinError(10,0.1680386);
   h1Ratio_Data->SetBinError(11,0.11227);
   h1Ratio_Data->SetBinError(12,0.104086);
   h1Ratio_Data->SetBinError(13,0.149005);
   h1Ratio_Data->SetBinError(14,0.1200458);
   h1Ratio_Data->SetBinError(15,0.1371201);
   h1Ratio_Data->SetBinError(16,0.1827793);
   h1Ratio_Data->SetBinError(17,0.1413815);
   h1Ratio_Data->SetBinError(18,0.1389749);
   h1Ratio_Data->SetBinError(19,0.1993516);
   h1Ratio_Data->SetBinError(20,0.1705377);
   h1Ratio_Data->SetBinError(21,0.1789688);
   h1Ratio_Data->SetBinError(22,0.1225363);
   h1Ratio_Data->SetBinError(23,0.1976336);
   h1Ratio_Data->SetBinError(24,0.1262623);
   h1Ratio_Data->SetBinError(25,0.1601798);
   h1Ratio_Data->SetBinError(26,0.04834921);
   h1Ratio_Data->SetMinimum(0);
   h1Ratio_Data->SetMaximum(2.2);
   h1Ratio_Data->SetEntries(686.9484);
   h1Ratio_Data->SetMarkerStyle(20);
   h1Ratio_Data->SetMarkerSize(0.8);
   h1Ratio_Data->GetXaxis()->SetTitle("p^{SA}_{T} / p^{RSA}_{T}");
   h1Ratio_Data->GetXaxis()->SetRange(1,100);
   h1Ratio_Data->GetXaxis()->SetLabelFont(42);
   h1Ratio_Data->GetXaxis()->SetTitleSize(0.048);
   h1Ratio_Data->GetXaxis()->SetTitleOffset(0.95);
   h1Ratio_Data->GetXaxis()->SetTitleFont(42);
   h1Ratio_Data->GetYaxis()->SetTitle("Arbitrary Units");
   h1Ratio_Data->GetYaxis()->SetLabelFont(42);
   h1Ratio_Data->GetYaxis()->SetTitleSize(0.048);
   h1Ratio_Data->GetYaxis()->SetTitleOffset(0.95);
   h1Ratio_Data->GetYaxis()->SetTitleFont(42);
   h1Ratio_Data->GetZaxis()->SetLabelFont(42);
   h1Ratio_Data->GetZaxis()->SetTitleSize(0.048);
   h1Ratio_Data->GetZaxis()->SetTitleFont(42);
   h1Ratio_Data->Draw("E");
   
   TH1F *h1Ratio_MC = new TH1F("h1Ratio_MC","PtBottom_recoD0_20_50",25,0,100);
   h1Ratio_MC->SetBinContent(7,1.695712);
   h1Ratio_MC->SetBinContent(8,2.702316);
   h1Ratio_MC->SetBinContent(9,1.639379);
   h1Ratio_MC->SetBinContent(10,1.07014);
   h1Ratio_MC->SetBinContent(11,0.8901455);
   h1Ratio_MC->SetBinContent(12,1.114204);
   h1Ratio_MC->SetBinContent(13,0.8666032);
   h1Ratio_MC->SetBinContent(14,0.7624239);
   h1Ratio_MC->SetBinContent(15,0.8418431);
   h1Ratio_MC->SetBinContent(16,0.7748783);
   h1Ratio_MC->SetBinContent(17,0.5828145);
   h1Ratio_MC->SetBinContent(18,0.6313823);
   h1Ratio_MC->SetBinContent(19,0.5357183);
   h1Ratio_MC->SetBinContent(20,1.043153);
   h1Ratio_MC->SetBinContent(21,0.6110151);
   h1Ratio_MC->SetBinContent(22,0.5411848);
   h1Ratio_MC->SetBinContent(23,0.9969195);
   h1Ratio_MC->SetBinContent(24,0.5051059);
   h1Ratio_MC->SetBinContent(25,0.4735367);
   h1Ratio_MC->SetBinContent(26,0.8857521);
   h1Ratio_MC->SetBinError(7,0.3785962);
   h1Ratio_MC->SetBinError(8,0.4629234);
   h1Ratio_MC->SetBinError(9,0.2889094);
   h1Ratio_MC->SetBinError(10,0.205704);
   h1Ratio_MC->SetBinError(11,0.1772469);
   h1Ratio_MC->SetBinError(12,0.2278815);
   h1Ratio_MC->SetBinError(13,0.1902175);
   h1Ratio_MC->SetBinError(14,0.1706841);
   h1Ratio_MC->SetBinError(15,0.2053887);
   h1Ratio_MC->SetBinError(16,0.1894325);
   h1Ratio_MC->SetBinError(17,0.1660731);
   h1Ratio_MC->SetBinError(18,0.1822644);
   h1Ratio_MC->SetBinError(19,0.1708695);
   h1Ratio_MC->SetBinError(20,0.3233941);
   h1Ratio_MC->SetBinError(21,0.1921783);
   h1Ratio_MC->SetBinError(22,0.2156132);
   h1Ratio_MC->SetBinError(23,0.3443318);
   h1Ratio_MC->SetBinError(24,0.2439893);
   h1Ratio_MC->SetBinError(25,0.2266885);
   h1Ratio_MC->SetBinError(26,0.08273763);
   h1Ratio_MC->SetEntries(274.3872);
   h1Ratio_MC->SetLineColor(2);
   h1Ratio_MC->SetMarkerColor(2);
   h1Ratio_MC->SetMarkerStyle(21);
   h1Ratio_MC->SetMarkerSize(0.8);
   h1Ratio_MC->GetXaxis()->SetRange(1,100);
   h1Ratio_MC->GetXaxis()->SetLabelFont(42);
   h1Ratio_MC->GetXaxis()->SetTitleSize(0.048);
   h1Ratio_MC->GetXaxis()->SetTitleOffset(1.2);
   h1Ratio_MC->GetXaxis()->SetTitleFont(42);
   h1Ratio_MC->GetYaxis()->SetLabelFont(42);
   h1Ratio_MC->GetYaxis()->SetTitleSize(0.048);
   h1Ratio_MC->GetYaxis()->SetTitleOffset(1.2);
   h1Ratio_MC->GetYaxis()->SetTitleFont(42);
   h1Ratio_MC->GetZaxis()->SetLabelFont(42);
   h1Ratio_MC->GetZaxis()->SetTitleSize(0.048);
   h1Ratio_MC->GetZaxis()->SetTitleFont(42);
   h1Ratio_MC->Draw("Esame");
   
   TLegend *leg = new TLegend(5.580966e-320,2.558766e-320,0,0,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","20 < |d_{0}| < 50 cm","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h1Ratio_Data","Cosmics data","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("h1Ratio_MC","Cosmics MC","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   cRatio->Modified();
   cRatio->cd();
   cRatio->SetSelected(cRatio);
}
