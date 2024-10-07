# procore_sdk.CoreCompanyDirectoryCompanyPermissionTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_permission_templates_get**](CoreCompanyDirectoryCompanyPermissionTemplatesApi.md#rest_v10_companies_company_id_permission_templates_get) | **GET** /rest/v1.0/companies/{company_id}/permission_templates | List permission templates
[**rest_v10_companies_company_id_permission_templates_id_get**](CoreCompanyDirectoryCompanyPermissionTemplatesApi.md#rest_v10_companies_company_id_permission_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/permission_templates/{id} | Returns specific template
[**rest_v10_companies_company_id_permission_templates_post**](CoreCompanyDirectoryCompanyPermissionTemplatesApi.md#rest_v10_companies_company_id_permission_templates_post) | **POST** /rest/v1.0/companies/{company_id}/permission_templates | Create Permission Template


# **rest_v10_companies_company_id_permission_templates_get**
> List[RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner] rest_v10_companies_company_id_permission_templates_get(procore_company_id, company_id, filters_type=filters_type, view=view)

List permission templates

Returns the Permission Template names and IDs for the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_permission_templates_get200_response_inner import RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyPermissionTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_type = 'filters_type_example' # str | Allows filtering by template type. If none is provided, default is \"project_tools\". Allowed types = company_tools, project_tools, global. Example - ?filters[type]=company_tools (optional)
    view = 'view_example' # str | Returns detailed permission templates if view=with_permissions is specified. (optional)

    try:
        # List permission templates
        api_response = api_instance.rest_v10_companies_company_id_permission_templates_get(procore_company_id, company_id, filters_type=filters_type, view=view)
        print("The response of CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_type** | **str**| Allows filtering by template type. If none is provided, default is \&quot;project_tools\&quot;. Allowed types &#x3D; company_tools, project_tools, global. Example - ?filters[type]&#x3D;company_tools | [optional] 
 **view** | **str**| Returns detailed permission templates if view&#x3D;with_permissions is specified. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_permission_templates_id_get**
> RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate rest_v10_companies_company_id_permission_templates_id_get(procore_company_id, company_id, id)

Returns specific template

Returns the Permission Template along with its permitted actions.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_permission_templates_post_request_permission_template import RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyPermissionTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | The ID of the permission template to be retrieved

    try:
        # Returns specific template
        api_response = api_instance.rest_v10_companies_company_id_permission_templates_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| The ID of the permission template to be retrieved | 

### Return type

[**RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate**](RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_permission_templates_post**
> RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate rest_v10_companies_company_id_permission_templates_post(procore_company_id, company_id, rest_v10_companies_company_id_permission_templates_post_request)

Create Permission Template

Returns the created Permission Template along with its permitted actions.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_permission_templates_post_request import RestV10CompaniesCompanyIdPermissionTemplatesPostRequest
from procore_sdk.models.rest_v10_companies_company_id_permission_templates_post_request_permission_template import RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyPermissionTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_permission_templates_post_request = procore_sdk.RestV10CompaniesCompanyIdPermissionTemplatesPostRequest() # RestV10CompaniesCompanyIdPermissionTemplatesPostRequest | 

    try:
        # Create Permission Template
        api_response = api_instance.rest_v10_companies_company_id_permission_templates_post(procore_company_id, company_id, rest_v10_companies_company_id_permission_templates_post_request)
        print("The response of CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyPermissionTemplatesApi->rest_v10_companies_company_id_permission_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_permission_templates_post_request** | [**RestV10CompaniesCompanyIdPermissionTemplatesPostRequest**](RestV10CompaniesCompanyIdPermissionTemplatesPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate**](RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

