# Auto generated configuration file
# using: 
# Revision: 1.381.2.13 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff.py --step GEN,SIM --filein powheg_Z_CT10nlo_1380_4000_100k.lhe --beamspot Realistic8TeVCollisionPPbBoost --conditions STARTHI53_V27::All --eventcontent RAWSIM --datatier GEN-SIM -n 100 --no_exec
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import datetime

process = cms.Process('GEN')
# var parsing # 
options = VarParsing.VarParsing ('standard')
options.maxEvents = 10

options.register('ptHatLow',
                 15,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Minimum pt-hat")

options.register('ptHatHigh',
                 1000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum pt-hat")

processType = 'NSD'

i = datetime.datetime.now()

otFile = 'GenJet_LO_R23475_5p02_%d_Powheg_analyzer_%d_pthat_%d_%s%s%s.root' % (options.maxEvents, options.ptHatLow,options.ptHatHigh, i.year, i.month, i.day)


ptmin          = str(options.ptHatLow)
ptmax          = str(options.ptHatHigh)


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
#process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealisticPPbBoost8TeVCollision_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic2p76TeV2013Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:pwgevents_sevil.lhe')
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)
'''
# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.13 $'),
    annotation = cms.untracked.string('Configuration/Generator/python/Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff.py nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff_py_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)
'''
###output TFile--------------------------------- 
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(otFile),
    #closeFileFast = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
#process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V27::All', '')
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
'''
# ============= Pythia setting  ================================
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
#from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
#from PythiaUEAMBT2Settings_cfi import *

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
                                 pythiaPylistVerbosity = cms.untracked.int32(0),
                                 filterEfficiency = cms.untracked.double(1.0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 comEnergy = cms.double(5020.0),
                                 # crossSection = cms.untracked.double(2980000000.0),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 PythiaParameters = cms.PSet(
                                         pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
                                                                        'MSTJ(22)=2     ! Decay those unstable particles', 
                                                                        'PARJ(71)=10 .  ! for which ctau  10 mm', 
                                                                        'MSTP(33)=0     ! no K factors in hard cross sections', 
                                                                        'MSTP(2)=1      ! which order running alphaS', 
                                                                        'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
                                                                        'MSTP(52)=2     ! work with LHAPDF', 
                                                                        'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
                                                                        #'PARP(89)=1800. ! sqrts for which PARP82 is set', 
                                                                        'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
                                                                        'MSTP(95)=6     ! CR (color reconnection parameters)', 
                                                                        'PARP(77)=1.016 ! CR', 
                                                                        'PARP(78)=0.538 ! CR', 
                                                                        'PARP(80)=0.1   ! Prob. colored parton from BBR', 
                                                                        'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
                                                                        'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
                                                                        'PARP(62)=1.025 ! ISR cutoff', 
                                                                        'MSTP(91)=1     ! Gaussian primordial kT', 
                                                                        'PARP(93)=10.0  ! primordial kT-max', 
                                                                        'MSTP(81)=20    ! multiple parton interactions 1 is Pythia default', 
                                                                        'MSTP(82)=4     ! Defines the multi-parton model',
                                                                        'MSTP(86)=1'	
                                                                        'MSTP(111) = 0'), #to set the mpi cut smaller than the pt of the hardest jet!
                                         processParameters = cms.vstring(
                                                 'MSEL=1   ! High Pt QCD',),
                                         parameterSets = cms.vstring('pythiaUESettings', 
                                                                     'processParameters')
                                 )
                         )

process.ProductionFilterSequence = cms.Sequence(process.generator)
# Path and EndPath definitions
'''
process.generation_step = cms.Path(process.pgen * process.genParticles)

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
    pythiaProcess = cms.string(processType),
    dijetEtaBins = cms.vdouble( -3.01, -2.63333, -2.07, -1.78833, -1.50667, -1.225, -0.943333, -0.661667, -0.38, -0.0983333, 0.183333, 0.465, 0.746667, 1.02833, 1.31, 1.59167, 1.87333, 2.43667, 3.0),
    dijetEtaWeights = cms.vdouble( 1, 0.772085, 0.701301, 0.753585, 0.813741, 0.882849, 0.943137, 0.977332, 0.993655, 1.0375, 1.04713, 1.04826, 1.05517, 1.05983, 1.0723, 1.06945, 1.01587, 1.41731 )    
)

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



process.ana_step = cms.Path(
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
)


#process.simulation_step = cms.Path(process.psim)
#process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genjet_step,process.genfiltersummary_step,process.simulation_step,process.ana_step,process.endjob_step)
process.schedule = cms.Schedule(process.generation_step,process.genjet_step,process.ana_step,process.endjob_step)


# Automatic addition of the customisation function

def customise(process):
	process.genParticles.abortOnUnknownPDGCode = False

	return(process)


# End of customisation function definition

process = customise(process)
