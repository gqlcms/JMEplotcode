#! /usr/bin/env python
import os
import glob
import math
import datetime
import array
import ROOT
import ntpath
import sys
import subprocess
from subprocess import Popen
from optparse   import OptionParser
from time       import gmtime, strftime
from array import array
print '\n';
from ROOT import gROOT, TPaveLabel, TPie, gStyle, gSystem, TGaxis, TStyle, TLatex, TString, TF1,TFile,TLine, TLegend, TH1D,TH2D,THStack, TGraph, TGraphErrors,TChain, TCanvas, TLorentzVector, TMatrixDSym, TMath, TText,TTree, TPad, TVectorD, RooFit, RooArgSet, RooArgList, RooArgSet, RooAbsData, RooAbsPdf, RooAddPdf, RooWorkspace, RooExtendPdf,RooCBShape, RooLandau, RooFFTConvPdf, RooGaussian, RooBifurGauss, RooArgusBG,RooDataSet, RooExponential,RooBreitWigner, RooVoigtian, RooNovosibirsk, RooRealVar,RooFormulaVar, RooDataHist, RooHist,RooCategory, RooChebychev, RooSimultaneous, RooGenericPdf,RooConstVar, RooKeysPdf, RooHistPdf, RooEffProd, RooProdPdf, TIter, kTRUE, kFALSE, kGray, kRed, kDashed, kGreen,kAzure, kOrange, kBlack,kBlue,kYellow,kCyan, kMagenta, kWhite


# open the file
myfile = TFile('output_updatejecs.root')

# retrieve the ntuple of interest
mychain = myfile.jmeanalyzer.Get("tree")
entries = mychain.GetEntriesFast()
#mychain.SetBranchAddress("_met", _mett)
h_PFmet  =TH1D("h_PFmet"  ,"met distributions",1000,0,5000);
h_qt_qt  =TH1D("h_qt_qt"  ,"qt distributions",100,10,100);
h_qt_up  =TH1D("h_qt_up"  ,"up distributions",100,10,100);
#h_qt_ratio  =TH1D("h_qt_ratio"  ,"ratio distributions",1000,0,1000);

total_entries = 0
total_entries1 = 0

for jentry in xrange(entries):
    total_entries = total_entries + 1
    mychain.GetEntry(jentry)    
    '''
    # get the next tree in the chain and verify
    ientry = mychain.LoadTree(jentry)
    if ientry < 0:
        break

    # copy next entry into memory and verify
    nb = mychain.GetEntry(jentry)
    if nb<=0:
        continue

    # use the values directly from the tree
    nEvent = int(mychain.ev)
    if nEvent<0:
        continue
    '''
    _met = mychain._met
    h_PFmet.Fill(_met)

# ------------ calculate QT
    _lPt = mychain._lPt
    _lEta = mychain._lEta
    _lPhi = mychain._lPhi
    _lenergy = mychain._lenergy

    _jetPt = mychain._jetRawPt
    _jetEta = mychain._jetEta
    _jetPhi = mychain._jetPhi
    _jetenergy = mychain._jetenergy

  #  print len(_jetPt)
    if ( (len(_lPt) != 0) & (len(_jetPt) != 0) ) :
       total_entries1 = total_entries1 + 1
       qt_l = TLorentzVector(0, 0, 0, 0)
       for i in range(0,len(_lPt)):
           qt_l1 = TLorentzVector(0, 0, 0, 0)
           qt_l1.SetPtEtaPhiE(_lPt[i], _lEta[i], _lPhi[i], _lenergy[i])
           qt_l += qt_l1
       qt_jet = TLorentzVector(0, 0, 0, 0)
       for i in range(0,len(_jetPt)):
           qt_jet1 = TLorentzVector(0, 0, 0, 0)
           qt_jet1.SetPtEtaPhiE(_jetPt[i], _jetEta[i], _jetPhi[i], _jetenergy[i])
           qt_jet += qt_jet1

       qt_l_x = qt_l.Px()
       qt_l_y = qt_l.Py()
       qt_jet_x = qt_jet.Px()
       qt_jet_y = qt_jet.Py()
       qt_dot = qt_l_x*qt_jet_x + qt_l_y*qt_jet_y        
       up = qt_dot/( qt_l.Pt())       
 
       h_qt_qt.Fill(abs(qt_l.Pt()),abs(qt_l.Pt()))
       h_qt_up.Fill(abs(qt_l.Pt()), abs(up))

       test = abs(qt_l.Pt())
       print "#########"
       print test
       print "-----"
       print up
       print "#########"
# ---------- save histogram --------------

print total_entries1
print "total_entries1"
print total_entries
print "total_entries"

A3 = TCanvas("A3","Plotting Canvas",150,10,990,660);
h_ratio_qt_up = h_qt_up.Clone("h_ratio_qt_up")
h_ratio_qt_up.Divide(h_qt_qt)
h_ratio_qt_up.Draw();
#h_qt_qt.Draw()
A3.SaveAs("h_ratio.jpg");
