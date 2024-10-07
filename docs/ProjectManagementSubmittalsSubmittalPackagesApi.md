# procore_sdk.ProjectManagementSubmittalsSubmittalPackagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_submittal_packages_get**](ProjectManagementSubmittalsSubmittalPackagesApi.md#rest_v10_projects_project_id_submittal_packages_get) | **GET** /rest/v1.0/projects/{project_id}/submittal_packages | List Submittal Packages on a project


# **rest_v10_projects_project_id_submittal_packages_get**
> List[RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage] rest_v10_projects_project_id_submittal_packages_get(procore_company_id, project_id, filters_id=filters_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List Submittal Packages on a project

Return a list of all Submittal Packages from a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package import RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Submittal Packages on a project
        api_response = api_instance.rest_v10_projects_project_id_submittal_packages_get(procore_company_id, project_id, filters_id=filters_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of ProjectManagementSubmittalsSubmittalPackagesApi->rest_v10_projects_project_id_submittal_packages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalPackagesApi->rest_v10_projects_project_id_submittal_packages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage]**](RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Submittal Packages listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

