# procore_sdk.ProjectManagementBiddingBidFormSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete**](ProjectManagementBiddingBidFormSectionsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_form_sections/{bid_form_section_id} | Delete Bid Form Section


# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete**
> rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete(procore_company_id, project_id, bid_package_id, bid_form_section_id)

Delete Bid Form Section

Delete single Bid Form Section.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_section_id = 56 # int | Bid Form Section ID

    try:
        # Delete Bid Form Section
        api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete(procore_company_id, project_id, bid_package_id, bid_form_section_id)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormSectionsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_form_sections_bid_form_section_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_section_id** | **int**| Bid Form Section ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form section to delete |  -  |
**422** | Can not delete due to errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

