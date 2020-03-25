# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CheckDomainAvailabilityParameter(Model):
    """Check Domain availability parameter.

    All required parameters must be populated in order to send to Azure.

    :param subdomain_name: Required. The subdomain name to use.
    :type subdomain_name: str
    :param type: Required. The Type of the resource.
    :type type: str
    """

    _validation = {
        'subdomain_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'subdomain_name': {'key': 'subdomainName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, subdomain_name: str, type: str, **kwargs) -> None:
        super(CheckDomainAvailabilityParameter, self).__init__(**kwargs)
        self.subdomain_name = subdomain_name
        self.type = type


class CheckDomainAvailabilityResult(Model):
    """Check Domain availability result.

    :param is_subdomain_available: Indicates the given SKU is available or
     not.
    :type is_subdomain_available: bool
    :param reason: Reason why the SKU is not available.
    :type reason: str
    :param subdomain_name: The subdomain name to use.
    :type subdomain_name: str
    :param type: The Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'is_subdomain_available': {'key': 'isSubdomainAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'subdomain_name': {'key': 'subdomainName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, is_subdomain_available: bool=None, reason: str=None, subdomain_name: str=None, type: str=None, **kwargs) -> None:
        super(CheckDomainAvailabilityResult, self).__init__(**kwargs)
        self.is_subdomain_available = is_subdomain_available
        self.reason = reason
        self.subdomain_name = subdomain_name
        self.type = type


class CheckSkuAvailabilityParameter(Model):
    """Check SKU availability parameter.

    All required parameters must be populated in order to send to Azure.

    :param skus: Required. The SKU of the resource.
    :type skus: list[str]
    :param kind: Required. The Kind of the resource.
    :type kind: str
    :param type: Required. The Type of the resource.
    :type type: str
    """

    _validation = {
        'skus': {'required': True},
        'kind': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'skus': {'key': 'skus', 'type': '[str]'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, skus, kind: str, type: str, **kwargs) -> None:
        super(CheckSkuAvailabilityParameter, self).__init__(**kwargs)
        self.skus = skus
        self.kind = kind
        self.type = type


class CheckSkuAvailabilityResult(Model):
    """Check SKU availability result.

    :param kind: The Kind of the resource.
    :type kind: str
    :param type: The Type of the resource.
    :type type: str
    :param sku_name: The SKU of Cognitive Services account.
    :type sku_name: str
    :param sku_available: Indicates the given SKU is available or not.
    :type sku_available: bool
    :param reason: Reason why the SKU is not available.
    :type reason: str
    :param message: Additional error message.
    :type message: str
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku_name': {'key': 'skuName', 'type': 'str'},
        'sku_available': {'key': 'skuAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, type: str=None, sku_name: str=None, sku_available: bool=None, reason: str=None, message: str=None, **kwargs) -> None:
        super(CheckSkuAvailabilityResult, self).__init__(**kwargs)
        self.kind = kind
        self.type = type
        self.sku_name = sku_name
        self.sku_available = sku_available
        self.reason = reason
        self.message = message


class CheckSkuAvailabilityResultList(Model):
    """Check SKU availability result list.

    :param value: Check SKU availability result list.
    :type value:
     list[~azure.mgmt.cognitiveservices.models.CheckSkuAvailabilityResult]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CheckSkuAvailabilityResult]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(CheckSkuAvailabilityResultList, self).__init__(**kwargs)
        self.value = value


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class CognitiveServicesAccount(Model):
    """Cognitive Services Account is an Azure resource representing the
    provisioned account, its type, location and SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar etag: Entity Tag
    :vartype etag: str
    :ivar id: The id of the created account
    :vartype id: str
    :param kind: The Kind of the resource.
    :type kind: str
    :param location: The location of the resource
    :type location: str
    :ivar name: The name of the created account
    :vartype name: str
    :param properties: Properties of Cognitive Services account.
    :type properties:
     ~azure.mgmt.cognitiveservices.models.CognitiveServicesAccountProperties
    :param sku: The SKU of Cognitive Services account.
    :type sku: ~azure.mgmt.cognitiveservices.models.Sku
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :ivar type: Resource type
    :vartype type: str
    :param identity: The identity of Cognitive Services account.
    :type identity: ~azure.mgmt.cognitiveservices.models.Identity
    """

    _validation = {
        'etag': {'readonly': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'CognitiveServicesAccountProperties'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, *, kind: str=None, location: str=None, properties=None, sku=None, tags=None, identity=None, **kwargs) -> None:
        super(CognitiveServicesAccount, self).__init__(**kwargs)
        self.etag = None
        self.id = None
        self.kind = kind
        self.location = location
        self.name = None
        self.properties = properties
        self.sku = sku
        self.tags = tags
        self.type = None
        self.identity = identity


class CognitiveServicesAccountApiProperties(Model):
    """The api properties for special APIs.

    :param qna_runtime_endpoint: (QnAMaker Only) The runtime endpoint of
     QnAMaker.
    :type qna_runtime_endpoint: str
    :param statistics_enabled: (Bing Search Only) The flag to enable
     statistics of Bing Search.
    :type statistics_enabled: bool
    :param event_hub_connection_string: (Personalization Only) The flag to
     enable statistics of Bing Search.
    :type event_hub_connection_string: str
    :param storage_account_connection_string: (Personalization Only) The
     storage account connection string.
    :type storage_account_connection_string: str
    """

    _validation = {
        'event_hub_connection_string': {'max_length': 1000, 'pattern': r'^( *)Endpoint=sb://(.*);( *)SharedAccessKeyName=(.*);( *)SharedAccessKey=(.*)$'},
        'storage_account_connection_string': {'max_length': 1000, 'pattern': r'^(( *)DefaultEndpointsProtocol=(http|https)( *);( *))?AccountName=(.*)AccountKey=(.*)EndpointSuffix=(.*)$'},
    }

    _attribute_map = {
        'qna_runtime_endpoint': {'key': 'qnaRuntimeEndpoint', 'type': 'str'},
        'statistics_enabled': {'key': 'statisticsEnabled', 'type': 'bool'},
        'event_hub_connection_string': {'key': 'eventHubConnectionString', 'type': 'str'},
        'storage_account_connection_string': {'key': 'storageAccountConnectionString', 'type': 'str'},
    }

    def __init__(self, *, qna_runtime_endpoint: str=None, statistics_enabled: bool=None, event_hub_connection_string: str=None, storage_account_connection_string: str=None, **kwargs) -> None:
        super(CognitiveServicesAccountApiProperties, self).__init__(**kwargs)
        self.qna_runtime_endpoint = qna_runtime_endpoint
        self.statistics_enabled = statistics_enabled
        self.event_hub_connection_string = event_hub_connection_string
        self.storage_account_connection_string = storage_account_connection_string


class CognitiveServicesAccountEnumerateSkusResult(Model):
    """The list of cognitive services accounts operation response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: Gets the list of Cognitive Services accounts and their
     properties.
    :vartype value:
     list[~azure.mgmt.cognitiveservices.models.CognitiveServicesResourceAndSku]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CognitiveServicesResourceAndSku]'},
    }

    def __init__(self, **kwargs) -> None:
        super(CognitiveServicesAccountEnumerateSkusResult, self).__init__(**kwargs)
        self.value = None


class CognitiveServicesAccountKeys(Model):
    """The access keys for the cognitive services account.

    :param key1: Gets the value of key 1.
    :type key1: str
    :param key2: Gets the value of key 2.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(self, *, key1: str=None, key2: str=None, **kwargs) -> None:
        super(CognitiveServicesAccountKeys, self).__init__(**kwargs)
        self.key1 = key1
        self.key2 = key2


class CognitiveServicesAccountProperties(Model):
    """Properties of Cognitive Services account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: Gets the status of the cognitive services
     account at the time the operation was called. Possible values include:
     'Creating', 'ResolvingDNS', 'Moving', 'Deleting', 'Succeeded', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.cognitiveservices.models.ProvisioningState
    :ivar endpoint: Endpoint of the created account.
    :vartype endpoint: str
    :ivar internal_id: The internal identifier.
    :vartype internal_id: str
    :param custom_sub_domain_name: Optional subdomain name used for
     token-based authentication.
    :type custom_sub_domain_name: str
    :param network_acls: A collection of rules governing the accessibility
     from specific network locations.
    :type network_acls: ~azure.mgmt.cognitiveservices.models.NetworkRuleSet
    :param encryption: The encryption properties for this resource.
    :type encryption: ~azure.mgmt.cognitiveservices.models.Encryption
    :param user_owned_storage: The storage accounts for this resource.
    :type user_owned_storage:
     list[~azure.mgmt.cognitiveservices.models.UserOwnedStorage]
    :param api_properties: The api properties for special APIs.
    :type api_properties:
     ~azure.mgmt.cognitiveservices.models.CognitiveServicesAccountApiProperties
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'endpoint': {'readonly': True},
        'internal_id': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'internal_id': {'key': 'internalId', 'type': 'str'},
        'custom_sub_domain_name': {'key': 'customSubDomainName', 'type': 'str'},
        'network_acls': {'key': 'networkAcls', 'type': 'NetworkRuleSet'},
        'encryption': {'key': 'encryption', 'type': 'Encryption'},
        'user_owned_storage': {'key': 'userOwnedStorage', 'type': '[UserOwnedStorage]'},
        'api_properties': {'key': 'apiProperties', 'type': 'CognitiveServicesAccountApiProperties'},
    }

    def __init__(self, *, custom_sub_domain_name: str=None, network_acls=None, encryption=None, user_owned_storage=None, api_properties=None, **kwargs) -> None:
        super(CognitiveServicesAccountProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.endpoint = None
        self.internal_id = None
        self.custom_sub_domain_name = custom_sub_domain_name
        self.network_acls = network_acls
        self.encryption = encryption
        self.user_owned_storage = user_owned_storage
        self.api_properties = api_properties


class CognitiveServicesResourceAndSku(Model):
    """Cognitive Services resource type and SKU.

    :param resource_type: Resource Namespace and Type
    :type resource_type: str
    :param sku: The SKU of Cognitive Services account.
    :type sku: ~azure.mgmt.cognitiveservices.models.Sku
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, resource_type: str=None, sku=None, **kwargs) -> None:
        super(CognitiveServicesResourceAndSku, self).__init__(**kwargs)
        self.resource_type = resource_type
        self.sku = sku


class Encryption(Model):
    """Properties to configure Encryption.

    :param key_vault_properties: Properties of KeyVault
    :type key_vault_properties:
     ~azure.mgmt.cognitiveservices.models.KeyVaultProperties
    :param key_source: Enumerates the possible value of keySource for
     Encryption. Possible values include: 'Microsoft.CognitiveServices',
     'Microsoft.KeyVault'. Default value: "Microsoft.KeyVault" .
    :type key_source: str or ~azure.mgmt.cognitiveservices.models.KeySource
    """

    _attribute_map = {
        'key_vault_properties': {'key': 'keyVaultProperties', 'type': 'KeyVaultProperties'},
        'key_source': {'key': 'keySource', 'type': 'str'},
    }

    def __init__(self, *, key_vault_properties=None, key_source="Microsoft.KeyVault", **kwargs) -> None:
        super(Encryption, self).__init__(**kwargs)
        self.key_vault_properties = key_vault_properties
        self.key_source = key_source


class Error(Model):
    """Cognitive Services error object.

    :param error: The error body.
    :type error: ~azure.mgmt.cognitiveservices.models.ErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.error = error


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)


class ErrorBody(Model):
    """Cognitive Services error body.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. error code
    :type code: str
    :param message: Required. error message
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str, message: str, **kwargs) -> None:
        super(ErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message


class Identity(Model):
    """Managed service identity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param type: Type of managed service identity. Possible values include:
     'None', 'SystemAssigned', 'UserAssigned'
    :type type: str or ~azure.mgmt.cognitiveservices.models.IdentityType
    :ivar tenant_id: Tenant of managed service identity.
    :vartype tenant_id: str
    :ivar principal_id: Principal Id of managed service identity.
    :vartype principal_id: str
    :param user_assigned_identities: The list of user assigned identities
     associated with the resource. The user identity dictionary key references
     will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.cognitiveservices.models.UserAssignedIdentity]
    """

    _validation = {
        'tenant_id': {'readonly': True},
        'principal_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'IdentityType'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserAssignedIdentity}'},
    }

    def __init__(self, *, type=None, user_assigned_identities=None, **kwargs) -> None:
        super(Identity, self).__init__(**kwargs)
        self.type = type
        self.tenant_id = None
        self.principal_id = None
        self.user_assigned_identities = user_assigned_identities


class IpRule(Model):
    """A rule governing the accessibility from a specific ip address or ip range.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. An IPv4 address range in CIDR notation, such as
     '124.56.78.91' (simple IP address) or '124.56.78.0/24' (all addresses that
     start with 124.56.78).
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str, **kwargs) -> None:
        super(IpRule, self).__init__(**kwargs)
        self.value = value


class KeyVaultProperties(Model):
    """Properties to configure keyVault Properties.

    :param key_name: Name of the Key from KeyVault
    :type key_name: str
    :param key_version: Version of the Key from KeyVault
    :type key_version: str
    :param key_vault_uri: Uri of KeyVault
    :type key_vault_uri: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'key_version': {'key': 'keyVersion', 'type': 'str'},
        'key_vault_uri': {'key': 'keyVaultUri', 'type': 'str'},
    }

    def __init__(self, *, key_name: str=None, key_version: str=None, key_vault_uri: str=None, **kwargs) -> None:
        super(KeyVaultProperties, self).__init__(**kwargs)
        self.key_name = key_name
        self.key_version = key_version
        self.key_vault_uri = key_vault_uri


class MetricName(Model):
    """A metric name.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The name of the metric.
    :vartype value: str
    :ivar localized_value: The friendly name of the metric.
    :vartype localized_value: str
    """

    _validation = {
        'value': {'readonly': True},
        'localized_value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MetricName, self).__init__(**kwargs)
        self.value = None
        self.localized_value = None


class NetworkRuleSet(Model):
    """A set of rules governing the network accessibility.

    :param default_action: The default action when no rule from ipRules and
     from virtualNetworkRules match. This is only used after the bypass
     property has been evaluated. Possible values include: 'Allow', 'Deny'
    :type default_action: str or
     ~azure.mgmt.cognitiveservices.models.NetworkRuleAction
    :param ip_rules: The list of IP address rules.
    :type ip_rules: list[~azure.mgmt.cognitiveservices.models.IpRule]
    :param virtual_network_rules: The list of virtual network rules.
    :type virtual_network_rules:
     list[~azure.mgmt.cognitiveservices.models.VirtualNetworkRule]
    """

    _attribute_map = {
        'default_action': {'key': 'defaultAction', 'type': 'str'},
        'ip_rules': {'key': 'ipRules', 'type': '[IpRule]'},
        'virtual_network_rules': {'key': 'virtualNetworkRules', 'type': '[VirtualNetworkRule]'},
    }

    def __init__(self, *, default_action=None, ip_rules=None, virtual_network_rules=None, **kwargs) -> None:
        super(NetworkRuleSet, self).__init__(**kwargs)
        self.default_action = default_action
        self.ip_rules = ip_rules
        self.virtual_network_rules = virtual_network_rules


class OperationDisplayInfo(Model):
    """The operation supported by Cognitive Services.

    :param description: The description of the operation.
    :type description: str
    :param operation: The action that users can perform, based on their
     permission level.
    :type operation: str
    :param provider: Service provider: Microsoft Cognitive Services.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, operation: str=None, provider: str=None, resource: str=None, **kwargs) -> None:
        super(OperationDisplayInfo, self).__init__(**kwargs)
        self.description = description
        self.operation = operation
        self.provider = provider
        self.resource = resource


class OperationEntity(Model):
    """The operation supported by Cognitive Services.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The operation supported by Cognitive Services.
    :type display: ~azure.mgmt.cognitiveservices.models.OperationDisplayInfo
    :param origin: The origin of the operation.
    :type origin: str
    :param properties: Additional properties.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, name: str=None, display=None, origin: str=None, properties=None, **kwargs) -> None:
        super(OperationEntity, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties


class RegenerateKeyParameters(Model):
    """Regenerate key parameters.

    All required parameters must be populated in order to send to Azure.

    :param key_name: Required. key name to generate (Key1|Key2). Possible
     values include: 'Key1', 'Key2'
    :type key_name: str or ~azure.mgmt.cognitiveservices.models.KeyName
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'KeyName'},
    }

    def __init__(self, *, key_name, **kwargs) -> None:
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = key_name


class ResourceSku(Model):
    """Describes an available Cognitive Services SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resource_type: The type of resource the SKU applies to.
    :vartype resource_type: str
    :ivar name: The name of SKU.
    :vartype name: str
    :ivar tier: Specifies the tier of Cognitive Services account.
    :vartype tier: str
    :ivar kind: The Kind of resources that are supported in this SKU.
    :vartype kind: str
    :ivar locations: The set of locations that the SKU is available.
    :vartype locations: list[str]
    :ivar restrictions: The restrictions because of which SKU cannot be used.
     This is empty if there are no restrictions.
    :vartype restrictions:
     list[~azure.mgmt.cognitiveservices.models.ResourceSkuRestrictions]
    """

    _validation = {
        'resource_type': {'readonly': True},
        'name': {'readonly': True},
        'tier': {'readonly': True},
        'kind': {'readonly': True},
        'locations': {'readonly': True},
        'restrictions': {'readonly': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'restrictions': {'key': 'restrictions', 'type': '[ResourceSkuRestrictions]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSku, self).__init__(**kwargs)
        self.resource_type = None
        self.name = None
        self.tier = None
        self.kind = None
        self.locations = None
        self.restrictions = None


class ResourceSkuRestrictionInfo(Model):
    """ResourceSkuRestrictionInfo.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar locations: Locations where the SKU is restricted
    :vartype locations: list[str]
    :ivar zones: List of availability zones where the SKU is restricted.
    :vartype zones: list[str]
    """

    _validation = {
        'locations': {'readonly': True},
        'zones': {'readonly': True},
    }

    _attribute_map = {
        'locations': {'key': 'locations', 'type': '[str]'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSkuRestrictionInfo, self).__init__(**kwargs)
        self.locations = None
        self.zones = None


class ResourceSkuRestrictions(Model):
    """Describes restrictions of a SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of restrictions. Possible values include: 'Location',
     'Zone'
    :vartype type: str or
     ~azure.mgmt.cognitiveservices.models.ResourceSkuRestrictionsType
    :ivar values: The value of restrictions. If the restriction type is set to
     location. This would be different locations where the SKU is restricted.
    :vartype values: list[str]
    :ivar restriction_info: The information about the restriction where the
     SKU cannot be used.
    :vartype restriction_info:
     ~azure.mgmt.cognitiveservices.models.ResourceSkuRestrictionInfo
    :ivar reason_code: The reason for restriction. Possible values include:
     'QuotaId', 'NotAvailableForSubscription'
    :vartype reason_code: str or
     ~azure.mgmt.cognitiveservices.models.ResourceSkuRestrictionsReasonCode
    """

    _validation = {
        'type': {'readonly': True},
        'values': {'readonly': True},
        'restriction_info': {'readonly': True},
        'reason_code': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'ResourceSkuRestrictionsType'},
        'values': {'key': 'values', 'type': '[str]'},
        'restriction_info': {'key': 'restrictionInfo', 'type': 'ResourceSkuRestrictionInfo'},
        'reason_code': {'key': 'reasonCode', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSkuRestrictions, self).__init__(**kwargs)
        self.type = None
        self.values = None
        self.restriction_info = None
        self.reason_code = None


class Sku(Model):
    """The SKU of the cognitive services account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the sku name. Required for account
     creation, optional for update.
    :type name: str
    :ivar tier: Gets the sku tier. This is based on the SKU name. Possible
     values include: 'Free', 'Standard', 'Premium'
    :vartype tier: str or ~azure.mgmt.cognitiveservices.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class Usage(Model):
    """The usage data for a usage request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param unit: The unit of the metric. Possible values include: 'Count',
     'Bytes', 'Seconds', 'Percent', 'CountPerSecond', 'BytesPerSecond',
     'Milliseconds'
    :type unit: str or ~azure.mgmt.cognitiveservices.models.UnitType
    :ivar name: The name information for the metric.
    :vartype name: ~azure.mgmt.cognitiveservices.models.MetricName
    :ivar quota_period: The quota period used to summarize the usage values.
    :vartype quota_period: str
    :ivar limit: Maximum value for this metric.
    :vartype limit: float
    :ivar current_value: Current value for this metric.
    :vartype current_value: float
    :ivar next_reset_time: Next reset time for current quota.
    :vartype next_reset_time: str
    :param status: Cognitive Services account quota usage status. Possible
     values include: 'Included', 'Blocked', 'InOverage', 'Unknown'
    :type status: str or ~azure.mgmt.cognitiveservices.models.QuotaUsageStatus
    """

    _validation = {
        'name': {'readonly': True},
        'quota_period': {'readonly': True},
        'limit': {'readonly': True},
        'current_value': {'readonly': True},
        'next_reset_time': {'readonly': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'MetricName'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
        'limit': {'key': 'limit', 'type': 'float'},
        'current_value': {'key': 'currentValue', 'type': 'float'},
        'next_reset_time': {'key': 'nextResetTime', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, unit=None, status=None, **kwargs) -> None:
        super(Usage, self).__init__(**kwargs)
        self.unit = unit
        self.name = None
        self.quota_period = None
        self.limit = None
        self.current_value = None
        self.next_reset_time = None
        self.status = status


class UsagesResult(Model):
    """The response to a list usage request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of usages for Cognitive Service account.
    :vartype value: list[~azure.mgmt.cognitiveservices.models.Usage]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(self, **kwargs) -> None:
        super(UsagesResult, self).__init__(**kwargs)
        self.value = None


class UserAssignedIdentity(Model):
    """User-assigned managed identity.

    :param principal_id: Azure Active Directory principal ID associated with
     this Identity.
    :type principal_id: str
    :param client_id: Client App Id associated with this identity.
    :type client_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, *, principal_id: str=None, client_id: str=None, **kwargs) -> None:
        super(UserAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = principal_id
        self.client_id = client_id


class UserOwnedStorage(Model):
    """The user owned storage for Cognitive Services account.

    :param resource_id: Full resource id of a Microsoft.Storage resource.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, *, resource_id: str=None, **kwargs) -> None:
        super(UserOwnedStorage, self).__init__(**kwargs)
        self.resource_id = resource_id


class VirtualNetworkRule(Model):
    """A rule governing the accessibility from a specific virtual network.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Full resource id of a vnet subnet, such as
     '/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1'.
    :type id: str
    :param state: Gets the state of virtual network rule.
    :type state: str
    :param ignore_missing_vnet_service_endpoint: Ignore missing vnet service
     endpoint or not.
    :type ignore_missing_vnet_service_endpoint: bool
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'ignore_missing_vnet_service_endpoint': {'key': 'ignoreMissingVnetServiceEndpoint', 'type': 'bool'},
    }

    def __init__(self, *, id: str, state: str=None, ignore_missing_vnet_service_endpoint: bool=None, **kwargs) -> None:
        super(VirtualNetworkRule, self).__init__(**kwargs)
        self.id = id
        self.state = state
        self.ignore_missing_vnet_service_endpoint = ignore_missing_vnet_service_endpoint
