# save starting directory
cwd=$PWD
# set cms software architecture
export SCRAM_ARCH=slc7_amd64_gcc700
# set cmssw version
cmssw_version=CMSSW_10_6_26
# get cmssw version
scram project $cmssw_version
cd $cmssw_version/src
# set cms environment
cmsenv
# merge changes necessary for custom nanoaod production
git-cms-merge-topic michaelwassmer:CMSSW_10_6_26_CustomNanoAODMonotop
# get jetToolbox for jet reclustering
git clone https://github.com/cms-jet/JetToolbox JMEAnalysis/JetToolbox -b jetToolbox_102X_v3
mkdir CustomNanoProd
cd CustomNanoProd
# get cmsDriver commands and configs
git clone https://github.com/michaelwassmer/CustomNanoProd
cd $CMSSW_BASE/src
scram b -j 10
# go back to starting directory
cd $cwd