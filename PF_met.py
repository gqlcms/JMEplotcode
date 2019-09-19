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
from ROOT import gROOT, TPaveLabel, TPie, gStyle, gSystem, TGaxis, TStyle, TLatex, TString, TF1,TFile,TLine, TLegend, TH1D,TH2D,THStack, TGraph, TGraphErrors,TChain, TCanvas, TMatrixDSym, TMath, TText,TTree, TPad, TVectorD, RooFit, RooArgSet, RooArgList, RooArgSet, RooAbsData, RooAbsPdf, RooAddPdf, RooWorkspace, RooExtendPdf,RooCBShape, RooLandau, RooFFTConvPdf, RooGaussian, RooBifurGauss, RooArgusBG,RooDataSet, RooExponential,RooBreitWigner, RooVoigtian, RooNovosibirsk, RooRealVar,RooFormulaVar, RooDataHist, RooHist,RooCategory, RooChebychev, RooSimultaneous, RooGenericPdf,RooConstVar, RooKeysPdf, RooHistPdf, RooEffProd, RooProdPdf, TIter, kTRUE, kFALSE, kGray, kRed, kDashed, kGreen,kAzure, kOrange, kBlack,kBlue,kYellow,kCyan, kMagenta, kWhite


# open the file
myfile = TFile('output_updatejecs.root')

# retrieve the ntuple of interest
mychain = myfile.jmeanalyzer.Get("tree")
entries = mychain.GetEntriesFast()
#mychain.SetBranchAddress("_met", _mett)
h_PFmet  =TH1D("h_PFmet"  ,"met distributions",1000,0,5000);
for jentry in xrange(entries):
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

A3 = TCanvas("A3","Plotting Canvas",150,10,990,660);
h_PFmet.Draw();
A3.SaveAs("PF_met.jpg");
