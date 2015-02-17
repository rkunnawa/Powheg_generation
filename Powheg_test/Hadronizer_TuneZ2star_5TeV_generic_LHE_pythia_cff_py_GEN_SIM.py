# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff.py --step GEN,SIM --filein file:powheg_Z_CT10nlo_1380_4000_100k.lhe --beamspot Realistic8TeVCollisionPPbBoost --conditions STARTHI53_V27::All --eventcontent RAWSIM --datatier GEN-SIM -n 1 --no_exec
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import os

process = cms.Process('GEN')
options = VarParsing.VarParsing ('standard')

options.output = 'Powheg_test_5TeV_Pythia_TuneZ2star_GEN_raghav_LHE_file.root'
options.maxEvents = 10

options.register('processType',
                 "NSD",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Pythia process type with pT_hat range")

options.register('sqrtS',
                 5020.0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Center-of-mass energy")

options.register('ptHatLow',
                 10,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Minimum pt-hat")

options.register('ptHatHigh',
                 1000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum pt-hat")

options.parseArguments()

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealisticPPbBoost8TeVCollision_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:pwgevents_raghav.lhe')
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('runs Z2 Pythia6'),
    name = cms.untracked.string('$Source:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/CMSSW_5_3_8_HI_patch2/src/Appeltel/GenJetCrossCheckAnalyzer/test/Powheg_test/Hadronizer_TuneZ2star_5TeV_generic_LHE_pythia_cff.py $')
)

# Output definition
process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.output)
)

'''
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Powheg_test_5TeV_Pythia_TuneZ2star_GEN_yaxian_LHE_file.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)
'''
# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V27::All', '')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    comEnergy = cms.double(5020.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0          ! User defined processes', 
            'PMAS(5,1)=4.4   ! b quark mass', 
            'PMAS(6,1)=172.4 ! t quark mass', 
            #'MSTP(86)=1      ! requires MPIs to be softer than the main interaction'
	    ),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

process.gen_step = cms.Path(process.generator
                            * process.genParticles )

# ============= Gen jet ================================
process.ak2GenJets = process.ak5GenJets.clone( rParam = 0.2 )
process.ak3GenJets = process.ak5GenJets.clone( rParam = 0.3 )
process.ak4GenJets = process.ak5GenJets.clone( rParam = 0.4 )
process.ak7GenJets = process.ak5GenJets.clone( rParam = 0.7 )

process.genjet_step = cms.Path(process.genJetParticles 
                               * process.ak2GenJets
                               * process.ak3GenJets
                               * process.ak4GenJets
                               * process.ak5GenJets
                               * process.ak7GenJets
)

# =============== Analysis =============================
process.ak3GenJetSpectrum = cms.EDAnalyzer('GenJetCrossCheckAnalyzer',
    genJetSrc = cms.InputTag("ak3GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    doCMatrix = cms.bool(True),
    doFlavor = cms.bool(False),
    flavorSrc = cms.InputTag("flavourByRef"),
    flavorId = cms.vint32(0),    
    jetsByAbsRapidity = cms.bool(False),
    etaMin = cms.double(-1.0),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.3),
    pthatMin = cms.double(options.ptHatLow),
    pthatMax = cms.double(options.ptHatHigh),
    ptBins = cms.vdouble( 3, 4, 5, 7, 9, 12, 15, 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,1000 ),
    pythiaProcess = cms.string(options.processType ),
    dijetEtaBins = cms.vdouble( -3.01, -2.63333, -2.07, -1.78833, -1.50667, -1.225, -0.943333, -0.661667, -0.38, -0.0983333, 0.183333, 0.465, 0.746667, 1.02833, 1.31, 1.59167, 1.87333, 2.43667, 3.0),
    dijetEtaWeights = cms.vdouble( 1, 0.772085, 0.701301, 0.753585, 0.813741, 0.882849, 0.943137, 0.977332, 0.993655, 1.0375, 1.04713, 1.04826, 1.05517, 1.05983, 1.0723, 1.06945, 1.01587, 1.41731 )    
)

#R=0.3 
process.ak3GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum.clone(
    doCMatrix = cms.bool(False)
)
process.ak3GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(2.0)
)
process.ak3GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.5),
    etaMax = cms.double(-2.0)
)
process.ak3GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(-1.5)
)
process.ak3GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.5),
    etaMax = cms.double(-1.0)
)
process.ak3GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.0),
    etaMax = cms.double(-0.5)
)
process.ak3GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-0.5),
    etaMax = cms.double(0.5)
)
process.ak3GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0)
)
process.ak3GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5)
)
process.ak3GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0)
)

#R=0.2
process.ak2GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)

#R=0.4
process.ak4GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)

#R=0.5
process.ak5GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)

#R=0.7
process.ak7GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)

process.ak5GenJetSpectrum_QCD10001_00_05 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.0),
    etaMax = cms.double(0.5),
    jetRadius = cms.double(0.5),
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,846,1684)
)

process.ak5GenJetSpectrum_QCD10001_05_10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,790,1684)
)

process.ak5GenJetSpectrum_QCD10001_10_15 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,1410 )
)

process.ak5GenJetSpectrum_QCD10001_15_20 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,1032 )
)

process.ak5GenJetSpectrum_QCD10001_20_25 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.0),
    etaMax = cms.double(2.5),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,737 )
)

process.ak5GenJetSpectrum_QCD10001_25_30 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.5),
    etaMax = cms.double(3.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,468 )
)


process.ak3GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)


process.ak4GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)

process.ak7GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)


process.ak7GenJetSpectrum_QCD11004_00_05 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.0),
    etaMax = cms.double(0.5),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1248,1327,1410,1497,1588,1784,2116 )
)

process.ak7GenJetSpectrum_QCD11004_05_10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1248,1327,1410,1784 )
)

process.ak7GenJetSpectrum_QCD11004_10_15 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5),
    jetRadius = cms.double(0.7),    
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1684 )
)

process.ak7GenJetSpectrum_QCD11004_15_20 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0),
    jetRadius = cms.double(0.7),    
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1248  )
)

process.ak7GenJetSpectrum_QCD11004_20_25 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.0),
    etaMax = cms.double(2.5),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,905  )
)

process.ak3GenJetSpectrum_QCD11004_00_05 = process.ak7GenJetSpectrum_QCD11004_00_05.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_05_10 = process.ak7GenJetSpectrum_QCD11004_05_10.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_10_15 = process.ak7GenJetSpectrum_QCD11004_10_15.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_15_20 = process.ak7GenJetSpectrum_QCD11004_15_20.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_20_25 = process.ak7GenJetSpectrum_QCD11004_20_25.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)

process.ana_step = cms.Path(
#    process.ak3GenJetSpectrum
    process.ak3GenJetSpectrum_n10_p10 * 
    process.ak3GenJetSpectrum_n20_p20 *
    process.ak3GenJetSpectrum_n25_n20 *
    process.ak3GenJetSpectrum_n20_n15 *
    process.ak3GenJetSpectrum_n15_n10 *
    process.ak3GenJetSpectrum_n10_n05 *
    process.ak3GenJetSpectrum_n05_p05 *
    process.ak3GenJetSpectrum_p05_p10 *
    process.ak3GenJetSpectrum_p10_p15 *
    process.ak3GenJetSpectrum_p15_p20 *

    process.ak2GenJetSpectrum_n10_p10 * 
    process.ak2GenJetSpectrum_n20_p20 *
    process.ak2GenJetSpectrum_n25_n20 *
    process.ak2GenJetSpectrum_n20_n15 *
    process.ak2GenJetSpectrum_n15_n10 *
    process.ak2GenJetSpectrum_n10_n05 *
    process.ak2GenJetSpectrum_n05_p05 *
    process.ak2GenJetSpectrum_p05_p10 *
    process.ak2GenJetSpectrum_p10_p15 *
    process.ak2GenJetSpectrum_p15_p20 *

    process.ak4GenJetSpectrum_n10_p10 * 
    process.ak4GenJetSpectrum_n20_p20 *
    process.ak4GenJetSpectrum_n25_n20 *
    process.ak4GenJetSpectrum_n20_n15 *
    process.ak4GenJetSpectrum_n15_n10 *
    process.ak4GenJetSpectrum_n10_n05 *
    process.ak4GenJetSpectrum_n05_p05 *
    process.ak4GenJetSpectrum_p05_p10 *
    process.ak4GenJetSpectrum_p10_p15 *
    process.ak4GenJetSpectrum_p15_p20 *

    process.ak5GenJetSpectrum_n10_p10 * 
    process.ak5GenJetSpectrum_n20_p20 *
    process.ak5GenJetSpectrum_n25_n20 *
    process.ak5GenJetSpectrum_n20_n15 *
    process.ak5GenJetSpectrum_n15_n10 *
    process.ak5GenJetSpectrum_n10_n05 *
    process.ak5GenJetSpectrum_n05_p05 *
    process.ak5GenJetSpectrum_p05_p10 *
    process.ak5GenJetSpectrum_p10_p15 *
    process.ak5GenJetSpectrum_p15_p20 *

    process.ak7GenJetSpectrum_n10_p10 * 
    process.ak7GenJetSpectrum_n20_p20 *
    process.ak7GenJetSpectrum_n25_n20 *
    process.ak7GenJetSpectrum_n20_n15 *
    process.ak7GenJetSpectrum_n15_n10 *
    process.ak7GenJetSpectrum_n10_n05 *
    process.ak7GenJetSpectrum_n05_p05 *
    process.ak7GenJetSpectrum_p05_p10 *
    process.ak7GenJetSpectrum_p10_p15 *
    process.ak7GenJetSpectrum_p15_p20 

#    process.ak5GenJetSpectrum_QCD10001_00_05 *
#    process.ak5GenJetSpectrum_QCD10001_05_10 *
#    process.ak5GenJetSpectrum_QCD10001_10_15 *
#    process.ak5GenJetSpectrum_QCD10001_15_20 *
#    process.ak5GenJetSpectrum_QCD10001_20_25 *
#    process.ak5GenJetSpectrum_QCD10001_25_30 *
#    process.ak3GenJetSpectrum_QCD10001_00_05 *
#    process.ak3GenJetSpectrum_QCD10001_05_10 *
#    process.ak3GenJetSpectrum_QCD10001_10_15 *
#    process.ak3GenJetSpectrum_QCD10001_15_20 *
#    process.ak3GenJetSpectrum_QCD10001_20_25 *
#    process.ak3GenJetSpectrum_QCD10001_25_30 *
#    process.ak4GenJetSpectrum_QCD10001_00_05 *
#    process.ak4GenJetSpectrum_QCD10001_05_10 *
#    process.ak4GenJetSpectrum_QCD10001_10_15 *
#    process.ak4GenJetSpectrum_QCD10001_15_20 *
#    process.ak4GenJetSpectrum_QCD10001_20_25 *
#    process.ak4GenJetSpectrum_QCD10001_25_30 *
#    process.ak7GenJetSpectrum_QCD10001_00_05 *
#    process.ak7GenJetSpectrum_QCD10001_05_10 *
#    process.ak7GenJetSpectrum_QCD10001_10_15 *
#    process.ak7GenJetSpectrum_QCD10001_15_20 *
#    process.ak7GenJetSpectrum_QCD10001_20_25 *
#    process.ak7GenJetSpectrum_QCD10001_25_30 *
#    process.ak7GenJetSpectrum_QCD11004_00_05 *
#    process.ak7GenJetSpectrum_QCD11004_05_10 *
#    process.ak7GenJetSpectrum_QCD11004_10_15 *
#    process.ak7GenJetSpectrum_QCD11004_15_20 *
#    process.ak7GenJetSpectrum_QCD11004_20_25 *
#    process.ak3GenJetSpectrum_QCD11004_00_05 *
#    process.ak3GenJetSpectrum_QCD11004_05_10 *
#    process.ak3GenJetSpectrum_QCD11004_10_15 *
#    process.ak3GenJetSpectrum_QCD11004_15_20 *
#    process.ak3GenJetSpectrum_QCD11004_20_25 
)

# Path and EndPath definitions
#process.generation_step = cms.Path(process.pgen)
#process.simulation_step = cms.Path(process.psim)
#process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
process.schedule = cms.Schedule(process.gen_step,process.genjet_step,process.ana_step)

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

