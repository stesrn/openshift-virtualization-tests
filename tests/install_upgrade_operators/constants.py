SECTION_TITLE = "section_title"
FILE_SUFFIX = "file_suffix"
HCO_CR_CERT_CONFIG_CA_KEY = "ca"
HCO_CR_CERT_CONFIG_KEY = "certConfig"
HCO_CR_CERT_CONFIG_SERVER_KEY = "server"
HCO_CR_CERT_CONFIG_DURATION_KEY = "duration"
HCO_CR_CERT_CONFIG_RENEW_BEFORE_KEY = "renewBefore"
SIDECAR_FEATURE_GATE_KEY = "Sidecar"
WORKLOADUPDATEMETHODS = "workloadUpdateMethods"
KEY_PATH_SEPARATOR = "->"
TEMPLATE_VALIDATOR = "templateValidator"
DEVELOPER_CONFIGURATION = "developerConfiguration"
# featuregates:
DEPLOY_KUBE_SECONDARY_DNS = "deployKubeSecondaryDNS"
DISABLE_MDEV_CONFIGURATION = "disableMDevConfiguration"
PERSISTENT_RESERVATION = "persistentReservation"
FG_DISABLED = False
FG_ENABLED = True

FEATUREGATES = "featureGates"
RESOURCE_TYPE_STR = "resource_type"
RESOURCE_NAME_STR = "resource_name"
RESOURCE_NAMESPACE_STR = "resource_namespace"
KEY_NAME_STR = "key_name"
EXPECTED_KUBEVIRT_HARDCODED_FEATUREGATES = [
    "CPUManager",
    "Snapshot",
    "HotplugVolumes",
    "ExpandDisks",
    "HostDevices",
    "VMExport",
    "KubevirtSeccompProfile",
    "VMPersistentState",
    "InstancetypeReferencePolicy",
    "WithHostModelCPU",
    "HypervStrictCheck",
]
EXPECTED_CDI_HARDCODED_FEATUREGATES = ["DataVolumeClaimAdoption", "HonorWaitForFirstConsumer", "WebhookPvcRendering"]
HCO_DEFAULT_FEATUREGATES = {
    DEPLOY_KUBE_SECONDARY_DNS: FG_DISABLED,
    DISABLE_MDEV_CONFIGURATION: FG_DISABLED,
    PERSISTENT_RESERVATION: FG_DISABLED,
    "alignCPUs": FG_DISABLED,
    "downwardMetrics": FG_DISABLED,
    "enableMultiArchCommonBootImageImport": FG_DISABLED,
}
CUSTOM_DATASOURCE_NAME = "custom-datasource"
WORKLOAD_UPDATE_STRATEGY_KEY_NAME = "workloadUpdateStrategy"
