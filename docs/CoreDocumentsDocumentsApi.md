# procore_sdk.CoreDocumentsDocumentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_documents_get**](CoreDocumentsDocumentsApi.md#rest_v10_companies_company_id_documents_get) | **GET** /rest/v1.0/companies/{company_id}/documents | Company Folder and File index
[**rest_v10_projects_project_id_documents_get**](CoreDocumentsDocumentsApi.md#rest_v10_projects_project_id_documents_get) | **GET** /rest/v1.0/projects/{project_id}/documents | Project Folder and File index


# **rest_v10_companies_company_id_documents_get**
> List[ExampleOfAFolderThatIsAFile] rest_v10_companies_company_id_documents_get(procore_company_id, company_id, view=view, sort=sort, filters_created_by_id=filters_created_by_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_document_type=filters_document_type, filters_file_type=filters_file_type, filters_is_in_recycle_bin=filters_is_in_recycle_bin, filters_search=filters_search, filters_folder_id=filters_folder_id, page=page, per_page=per_page)

Company Folder and File index

Return a list of all folders and files in the company

### Example


```python
import procore_sdk
from procore_sdk.models.example_of_a_folder_that_is_a_file import ExampleOfAFolderThatIsAFile
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
    api_instance = procore_sdk.CoreDocumentsDocumentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | Determines how much information to include in the response. `normal` is the default, `extended` provides additional data. The example below shows the `extended` response. (optional)
    sort = 'sort_example' # str | Field to sort by. If the field is passed with a - (EX: -updated_at) it is sorted in reverse order (optional)
    filters_created_by_id = [56] # List[int] | Return item(s) created by the specified User IDs (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_document_type = 'filters_document_type_example' # str | Return item(s) that are file or folder (optional)
    filters_file_type = ['[\"pdf\",\"txt\"]'] # List[str] | Return item(s) that have the file extensions (optional)
    filters_is_in_recycle_bin = True # bool | Return item(s) that are in or not in the recycle bin (optional)
    filters_search = 'filters_search_example' # str | Return item(s) that contain string in document name and file description (optional)
    filters_folder_id = 26 # int | Returns the folder for a given id with all subfolders and subfiles up to a depth of 100.  Depths greater than 100 will need multiple queries to get all children. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # Company Folder and File index
        api_response = api_instance.rest_v10_companies_company_id_documents_get(procore_company_id, company_id, view=view, sort=sort, filters_created_by_id=filters_created_by_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_document_type=filters_document_type, filters_file_type=filters_file_type, filters_is_in_recycle_bin=filters_is_in_recycle_bin, filters_search=filters_search, filters_folder_id=filters_folder_id, page=page, per_page=per_page)
        print("The response of CoreDocumentsDocumentsApi->rest_v10_companies_company_id_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreDocumentsDocumentsApi->rest_v10_companies_company_id_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| Determines how much information to include in the response. &#x60;normal&#x60; is the default, &#x60;extended&#x60; provides additional data. The example below shows the &#x60;extended&#x60; response. | [optional] 
 **sort** | **str**| Field to sort by. If the field is passed with a - (EX: -updated_at) it is sorted in reverse order | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Return item(s) created by the specified User IDs | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_document_type** | **str**| Return item(s) that are file or folder | [optional] 
 **filters_file_type** | [**List[str]**](str.md)| Return item(s) that have the file extensions | [optional] 
 **filters_is_in_recycle_bin** | **bool**| Return item(s) that are in or not in the recycle bin | [optional] 
 **filters_search** | **str**| Return item(s) that contain string in document name and file description | [optional] 
 **filters_folder_id** | **int**| Returns the folder for a given id with all subfolders and subfiles up to a depth of 100.  Depths greater than 100 will need multiple queries to get all children. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ExampleOfAFolderThatIsAFile]**](ExampleOfAFolderThatIsAFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_documents_get**
> List[ExampleOfAFolderThatIsAFile] rest_v10_projects_project_id_documents_get(procore_company_id, project_id, view=view, sort=sort, filters_created_by_id=filters_created_by_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_document_type=filters_document_type, filters_file_type=filters_file_type, filters_is_in_recycle_bin=filters_is_in_recycle_bin, filters_search=filters_search, filters_folder_id=filters_folder_id, filters_custom_tag_ids=filters_custom_tag_ids, page=page, per_page=per_page)

Project Folder and File index

Return a list of all folders and files in the project

### Example


```python
import procore_sdk
from procore_sdk.models.example_of_a_folder_that_is_a_file import ExampleOfAFolderThatIsAFile
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
    api_instance = procore_sdk.CoreDocumentsDocumentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Determines how much information to include in the response. `normal` is the default, `extended` provides additional data. The example below shows the `extended` response. (optional)
    sort = 'sort_example' # str | Field to sort by. If the field is passed with a - (EX: -updated_at) it is sorted in reverse order (optional)
    filters_created_by_id = [56] # List[int] | Return item(s) created by the specified User IDs (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_document_type = 'filters_document_type_example' # str | Return item(s) that are file or folder (optional)
    filters_file_type = ['[\"pdf\",\"txt\"]'] # List[str] | Return item(s) that have the file extensions (optional)
    filters_is_in_recycle_bin = True # bool | Return item(s) that are in or not in the recycle bin (optional)
    filters_search = 'filters_search_example' # str | Return item(s) that contain string in document name and file description (optional)
    filters_folder_id = 26 # int | Returns the folder for a given id with all subfolders and subfiles up to a depth of 100.  Depths greater than 100 will need multiple queries to get all children. (optional)
    filters_custom_tag_ids = [56] # List[int] | Return item(s) with specified custom tag IDs (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # Project Folder and File index
        api_response = api_instance.rest_v10_projects_project_id_documents_get(procore_company_id, project_id, view=view, sort=sort, filters_created_by_id=filters_created_by_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_document_type=filters_document_type, filters_file_type=filters_file_type, filters_is_in_recycle_bin=filters_is_in_recycle_bin, filters_search=filters_search, filters_folder_id=filters_folder_id, filters_custom_tag_ids=filters_custom_tag_ids, page=page, per_page=per_page)
        print("The response of CoreDocumentsDocumentsApi->rest_v10_projects_project_id_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreDocumentsDocumentsApi->rest_v10_projects_project_id_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Determines how much information to include in the response. &#x60;normal&#x60; is the default, &#x60;extended&#x60; provides additional data. The example below shows the &#x60;extended&#x60; response. | [optional] 
 **sort** | **str**| Field to sort by. If the field is passed with a - (EX: -updated_at) it is sorted in reverse order | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Return item(s) created by the specified User IDs | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_document_type** | **str**| Return item(s) that are file or folder | [optional] 
 **filters_file_type** | [**List[str]**](str.md)| Return item(s) that have the file extensions | [optional] 
 **filters_is_in_recycle_bin** | **bool**| Return item(s) that are in or not in the recycle bin | [optional] 
 **filters_search** | **str**| Return item(s) that contain string in document name and file description | [optional] 
 **filters_folder_id** | **int**| Returns the folder for a given id with all subfolders and subfiles up to a depth of 100.  Depths greater than 100 will need multiple queries to get all children. | [optional] 
 **filters_custom_tag_ids** | [**List[int]**](int.md)| Return item(s) with specified custom tag IDs | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ExampleOfAFolderThatIsAFile]**](ExampleOfAFolderThatIsAFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

