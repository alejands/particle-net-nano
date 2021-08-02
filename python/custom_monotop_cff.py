##################################################################################
# This customization config is based on the custom JetMET NanoAOD step and used
# to add AK15PFPuppi jets to the NanoAOD tuples for the CMS mono-top analysis
##################################################################################

# import custom jme NanoAOD config
from PhysicsTools.NanoAOD.custom_jme_cff import *
# import ParticleNET discriminators (at the moment ParticleNET still for AK8Puppi)
from RecoBTag.ONNXRuntime.pfParticleNet_cff import _pfParticleNetJetTagsAll as pfParticleNetJetTagsAll

# edit the genjet config from the custom jme nanoaod config
# deactivate every preexisting genjet collection
for jet_config in config_genjets:
    jet_config["enabled"] = False

# add a new AK15 genjet collection
config_genjets.append(
    {
        "jet"     : "ak15gen",    
        "enabled" : True
    }
)

# remove all disabled genjet collections from the list of genjet collections
config_genjets = list(filter(lambda k: k['enabled'], config_genjets))

# add a necessary information object for the new AK15 genjet collection
nanoInfo_genjets["ak15gen"] = {
    "name" : "GenJetAK15",
    "doc"  : "AK15 Gen jets"
}

# edit the recojet config from the custom jme nanoaod config
# deactivate every preexisting genjet collection
for jet_config in config_recojets:
    jet_config["enabled"] = False

# add a new AK15 recojet collection
config_recojets.append(
    {
        "jet" : "ak15pfpuppi",
        "enabled" : True,
        "inputCollection" : "",
        "genJetsCollection" : "AK15GenJetsNoNu",
        "bTagDiscriminators" : pfParticleNetJetTagsAll
    }
)

# remove all disabled recojet collections from the list of recojet collections
config_recojets = list(filter(lambda k: k['enabled'], config_recojets))

# add a necessary information object for the new AK15 recojet collection
nanoInfo_recojets["ak15pfpuppi"] = {
    "name"  : "SuperFatJetPuppi",
    "doc"   : "AK15 PF Puppi jets with AK8 JECs applied, after basic selection (pt > 150)",
    "ptcut" : "pt > 150"
    }

# parameter set to store ParticleNET variable information for flattableproducer of nanoaod step
PARTICLENETAK15VARS = cms.PSet(
    particleNetAK15_TvsQCD = Var("bDiscriminator('pfParticleNetDiscriminatorsJetTags:TvsQCD')",float,doc="ParticleNetAK15 tagger Top vs QCD discriminator",precision=10),
    particleNetAK15_WvsQCD = Var("bDiscriminator('pfParticleNetDiscriminatorsJetTags:WvsQCD')",float,doc="ParticleNetAK15 tagger W vs QCD discriminator",precision=10),
    particleNetAK15_Tbcq = Var("bDiscriminator('pfParticleNetJetTags:probTbcq')",float,doc="ParticleNetAK15 tagger Tbcq node output",precision=10),
    particleNetAK15_Tbqq = Var("bDiscriminator('pfParticleNetJetTags:probTbqq')",float,doc="ParticleNetAK15 tagger Tbqq node output",precision=10),
    particleNetAK15_Tbc = Var("bDiscriminator('pfParticleNetJetTags:probTbc')",float,doc="ParticleNetAK15 tagger Tbc node output",precision=10),
    particleNetAK15_Tbq = Var("bDiscriminator('pfParticleNetJetTags:probTbq')",float,doc="ParticleNetAK15 tagger Tbq node output",precision=10),
    particleNetAK15_Tbel = Var("bDiscriminator('pfParticleNetJetTags:probTbel')",float,doc="ParticleNetAK15 tagger Tbel node output",precision=10),
    particleNetAK15_Tbmu = Var("bDiscriminator('pfParticleNetJetTags:probTbmu')",float,doc="ParticleNetAK15 tagger Tbmu node output",precision=10),
    particleNetAK15_Tbta = Var("bDiscriminator('pfParticleNetJetTags:probTbta')",float,doc="ParticleNetAK15 tagger Tbta node output",precision=10),
    particleNetAK15_Wcq = Var("bDiscriminator('pfParticleNetJetTags:probWcq')",float,doc="ParticleNetAK15 tagger Wcq node output",precision=10),
    particleNetAK15_Wqq = Var("bDiscriminator('pfParticleNetJetTags:probWqq')",float,doc="ParticleNetAK15 tagger Wqq node output",precision=10),
    particleNetAK15_QCDbb = Var("bDiscriminator('pfParticleNetJetTags:probQCDbb')",float,doc="ParticleNetAK15 tagger QCDbb node output",precision=10),
    particleNetAK15_QCDcc = Var("bDiscriminator('pfParticleNetJetTags:probQCDcc')",float,doc="ParticleNetAK15 tagger QCDcc node output",precision=10),
    particleNetAK15_QCDb = Var("bDiscriminator('pfParticleNetJetTags:probQCDb')",float,doc="ParticleNetAK15 tagger QCDb node output",precision=10),
    particleNetAK15_QCDc = Var("bDiscriminator('pfParticleNetJetTags:probQCDc')",float,doc="ParticleNetAK15 tagger QCDc node output",precision=10),
    particleNetAK15_QCDothers = Var("bDiscriminator('pfParticleNetJetTags:probQCDothers')",float,doc="ParticleNetAK15 tagger QCDothers node output",precision=10),
)

# use previous parameter set in this function to add the variables to the tableproducer
def AddParticleNetAK15Scores(proc, jetTableName=""):
    """
    Store ParticleNetAK15 scores in jetTable
    """

    getattr(proc, jetTableName).variables.particleNetAK15_TvsQCD = PARTICLENETAK15VARS.particleNetAK15_TvsQCD
    getattr(proc, jetTableName).variables.particleNetAK15_WvsQCD = PARTICLENETAK15VARS.particleNetAK15_WvsQCD
    getattr(proc, jetTableName).variables.particleNetAK15_Tbcq = PARTICLENETAK15VARS.particleNetAK15_Tbcq
    getattr(proc, jetTableName).variables.particleNetAK15_Tbqq = PARTICLENETAK15VARS.particleNetAK15_Tbqq
    getattr(proc, jetTableName).variables.particleNetAK15_Tbc = PARTICLENETAK15VARS.particleNetAK15_Tbc
    getattr(proc, jetTableName).variables.particleNetAK15_Tbq = PARTICLENETAK15VARS.particleNetAK15_Tbq
    getattr(proc, jetTableName).variables.particleNetAK15_Wcq = PARTICLENETAK15VARS.particleNetAK15_Wcq
    getattr(proc, jetTableName).variables.particleNetAK15_Wqq = PARTICLENETAK15VARS.particleNetAK15_Wqq
    getattr(proc, jetTableName).variables.particleNetAK15_QCDbb = PARTICLENETAK15VARS.particleNetAK15_QCDbb
    getattr(proc, jetTableName).variables.particleNetAK15_QCDcc = PARTICLENETAK15VARS.particleNetAK15_QCDcc
    getattr(proc, jetTableName).variables.particleNetAK15_QCDb = PARTICLENETAK15VARS.particleNetAK15_QCDb
    getattr(proc, jetTableName).variables.particleNetAK15_QCDc = PARTICLENETAK15VARS.particleNetAK15_QCDc
    getattr(proc, jetTableName).variables.particleNetAK15_QCDothers = PARTICLENETAK15VARS.particleNetAK15_QCDothers

    return proc

#===========================================================================
#
# MONOTOP CUSTOMIZATION function
#
#===========================================================================
def PrepMonoTopCustomNanoAOD(process,runOnMC):
  
    ###########################################################################
    #
    # Gen-level jets related functions. Only for MC.
    #
    ###########################################################################
    genJA = GenJetAdder()
    if runOnMC:
        ###########################################################################
        # Add additional GEN jets to NanoAOD
        ###########################################################################
        for jetConfig in config_genjets:
            cfg = { k : v for k, v in jetConfig.items() if k != "enabled"}
            genJetInfo = genJA.addGenJetCollection(process, **cfg)
            AddNewGenJets(process, genJetInfo)

    ###########################################################################
    #
    # Reco-level jets related functions. For both MC and data.
    #
    ###########################################################################
    recoJA = RecoJetAdder(runOnMC=runOnMC)
    ###########################################################################
    # Add additional Reco jets to NanoAOD
    ###########################################################################
    for jetConfig in config_recojets:
        cfg = { k : v for k, v in jetConfig.items() if k != "enabled"}
        recoJetInfo = recoJA.addRecoJetCollection(process, **cfg)
        AddNewPatJets(process, recoJetInfo, runOnMC)
    
    # overwrite the jet correction factors of the AK15PFPuppi jets to the AK8PFPuppi ones because AK15 factors don't exist
    process.jetCorrFactorsNanoAK15PFPUPPI.payload = cms.string('AK8PFPuppi')
    process.patJetCorrFactorsAK15PFPUPPIFinal.payload = cms.string('AK8PFPuppi')
    process.patJetCorrFactorsAK15PFPUPPIRecluster.payload = cms.string('AK8PFPuppi')
    process.patJetCorrFactorsTransientCorrectedAK15PFPUPPIFinal.payload = cms.string('AK8PFPuppi')
    
    # add ParticleNET information to the NanoAOD ntuples (at the moment ParticleNET still for AK8PFPuppi)
    AddParticleNetAK15Scores(process,"jetAK15PFPUPPITable")
    
    ###########################################################################
    # Save Maximum of Pt Hat Max
    ###########################################################################
    if runOnMC:
        process.puTable.savePtHatMax = True
  
    return process

# customization function for simulation
def PrepMonoTopCustomNanoAOD_MC(process):
    PrepMonoTopCustomNanoAOD(process,runOnMC=True)
    return process

# customization function for data
def PrepMonoTopCustomNanoAOD_Data(process):
    PrepMonoTopCustomNanoAOD(process,runOnMC=False)
    return process