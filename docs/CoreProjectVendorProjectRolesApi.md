# procore_sdk.CoreProjectVendorProjectRolesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_vendor_project_roles_id_patch**](CoreProjectVendorProjectRolesApi.md#rest_v10_projects_project_id_vendor_project_roles_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/vendor_project_roles/{id} | Update Vendor Project Roles


# **rest_v10_projects_project_id_vendor_project_roles_id_patch**
> VendorProjectRole rest_v10_projects_project_id_vendor_project_roles_id_patch(procore_company_id, id, project_id, body5=body5)

Update Vendor Project Roles

Set which Vendors are associated with a specific Project Role. Will remove any vendors associated with the role if they are not included in the `vendor_ids` parameter.

### Example


```python
import procore_sdk
from procore_sdk.models.body5 import Body5
from procore_sdk.models.vendor_project_role import VendorProjectRole
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
    api_instance = procore_sdk.CoreProjectVendorProjectRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Project Role
    project_id = 56 # int | Unique identifier for the project.
    body5 = procore_sdk.Body5() # Body5 |  (optional)

    try:
        # Update Vendor Project Roles
        api_response = api_instance.rest_v10_projects_project_id_vendor_project_roles_id_patch(procore_company_id, id, project_id, body5=body5)
        print("The response of CoreProjectVendorProjectRolesApi->rest_v10_projects_project_id_vendor_project_roles_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectVendorProjectRolesApi->rest_v10_projects_project_id_vendor_project_roles_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Project Role | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body5** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**VendorProjectRole**](VendorProjectRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

