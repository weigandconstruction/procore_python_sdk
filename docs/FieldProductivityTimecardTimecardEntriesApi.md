# procore_sdk.FieldProductivityTimecardTimecardEntriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_timecard_entries_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_get) | **GET** /rest/v1.0/companies/{company_id}/timecard_entries | List timecard entries (Company)
[**rest_v10_companies_company_id_timecard_entries_id_change_history_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_id_change_history_get) | **GET** /rest/v1.0/companies/{company_id}/timecard_entries/{id}/change_history | Show timecard entry change history (Company)
[**rest_v10_companies_company_id_timecard_entries_id_delete**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/timecard_entries/{id} | Delete timecard entry (Company)
[**rest_v10_companies_company_id_timecard_entries_id_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_id_get) | **GET** /rest/v1.0/companies/{company_id}/timecard_entries/{id} | Show timecard entry (Company)
[**rest_v10_companies_company_id_timecard_entries_id_patch**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/timecard_entries/{id} | Update timecard entry (Company)
[**rest_v10_companies_company_id_timecard_entries_post**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_companies_company_id_timecard_entries_post) | **POST** /rest/v1.0/companies/{company_id}/timecard_entries | Create timecard entry (Company)
[**rest_v10_projects_project_id_timecard_entries_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_get) | **GET** /rest/v1.0/projects/{project_id}/timecard_entries | List timecard entries (Project)
[**rest_v10_projects_project_id_timecard_entries_id_delete**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/timecard_entries/{id} | Delete timecard entry (Project)
[**rest_v10_projects_project_id_timecard_entries_id_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_id_get) | **GET** /rest/v1.0/projects/{project_id}/timecard_entries/{id} | Show timecard entry (Project)
[**rest_v10_projects_project_id_timecard_entries_id_patch**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/timecard_entries/{id} | Update timecard entry (Project)
[**rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch) | **PATCH** /rest/v1.0/projects/{project_id}/timecard_entries/{id}/remove_signature | Remove signature from timecard entry (Project)
[**rest_v10_projects_project_id_timecard_entries_id_sign_patch**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_id_sign_patch) | **PATCH** /rest/v1.0/projects/{project_id}/timecard_entries/{id}/sign | Update timecard entry signature (Project)
[**rest_v10_projects_project_id_timecard_entries_post**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_projects_project_id_timecard_entries_post) | **POST** /rest/v1.0/projects/{project_id}/timecard_entries | Create timecard entry (Project)
[**rest_v10_timecard_entries_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_timecard_entries_get) | **GET** /rest/v1.0/timecard_entries | List timecard entries
[**rest_v10_timecard_entries_id_delete**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_timecard_entries_id_delete) | **DELETE** /rest/v1.0/timecard_entries/{id} | Delete timecard entry
[**rest_v10_timecard_entries_id_get**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_timecard_entries_id_get) | **GET** /rest/v1.0/timecard_entries/{id} | Show timecard entry
[**rest_v10_timecard_entries_id_patch**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_timecard_entries_id_patch) | **PATCH** /rest/v1.0/timecard_entries/{id} | Update timecard entry
[**rest_v10_timecard_entries_post**](FieldProductivityTimecardTimecardEntriesApi.md#rest_v10_timecard_entries_post) | **POST** /rest/v1.0/timecard_entries | Create timecard entry


# **rest_v10_companies_company_id_timecard_entries_get**
> List[RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner] rest_v10_companies_company_id_timecard_entries_get(procore_company_id, company_id, filters_id=filters_id, filters_party_id=filters_party_id, filters_in_progress_only=filters_in_progress_only, filters_include_in_progress=filters_include_in_progress, filters_updated_at=filters_updated_at, page=page, per_page=per_page, start_date=start_date, end_date=end_date, start_time_in=start_time_in, end_time_in=end_time_in, use_filter_tz=use_filter_tz, serializer_view=serializer_view)

List timecard entries (Company)

Return a list of all Timecard Entries, serialized according to the MyTime field set

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_party_id = [56] # List[int] | Return item(s) with the specified Party ID. (optional)
    filters_in_progress_only = True # bool | Return work in progress item(s). (optional)
    filters_include_in_progress = True # bool | Return available and work in progress item(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    start_date = '2013-10-20' # date | The beginning of the date range for entries. (YYYY-MM-DD) (optional)
    end_date = '2013-10-20' # date | The ending of the date range for entries. (YYYY-MM-DD) (optional)
    start_time_in = 'start_time_in_example' # str | The beginning of the time_in range for entries (YYYY-MM-DDTHH:MM:SSZ). \"Z\" represents the timezone offset (i.e. -08:00, -0800). Optionally you may pass the literal \"Z\" which also means \"UTC\". (optional)
    end_time_in = 'end_time_in_example' # str | The ending of the time_in range for entries (YYYY-MM-DDTHH:MM:SSZ). \"Z\" represents the timezone offset (i.e. -08:00, -0800). Optionally you may pass the literal \"Z\" which also means \"UTC\". (optional)
    use_filter_tz = 'use_filter_tz_example' # str | When passed as \"true\" the timezone from start_time_in or end_time_in will be used for all timestamps in the response. Otherwise they'll use UTC. (optional)
    serializer_view = 'serializer_view_example' # str | Changes what fields are included in the response. (optional)

    try:
        # List timecard entries (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_get(procore_company_id, company_id, filters_id=filters_id, filters_party_id=filters_party_id, filters_in_progress_only=filters_in_progress_only, filters_include_in_progress=filters_include_in_progress, filters_updated_at=filters_updated_at, page=page, per_page=per_page, start_date=start_date, end_date=end_date, start_time_in=start_time_in, end_time_in=end_time_in, use_filter_tz=use_filter_tz, serializer_view=serializer_view)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_party_id** | [**List[int]**](int.md)| Return item(s) with the specified Party ID. | [optional] 
 **filters_in_progress_only** | **bool**| Return work in progress item(s). | [optional] 
 **filters_include_in_progress** | **bool**| Return available and work in progress item(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **start_date** | **date**| The beginning of the date range for entries. (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| The ending of the date range for entries. (YYYY-MM-DD) | [optional] 
 **start_time_in** | **str**| The beginning of the time_in range for entries (YYYY-MM-DDTHH:MM:SSZ). \&quot;Z\&quot; represents the timezone offset (i.e. -08:00, -0800). Optionally you may pass the literal \&quot;Z\&quot; which also means \&quot;UTC\&quot;. | [optional] 
 **end_time_in** | **str**| The ending of the time_in range for entries (YYYY-MM-DDTHH:MM:SSZ). \&quot;Z\&quot; represents the timezone offset (i.e. -08:00, -0800). Optionally you may pass the literal \&quot;Z\&quot; which also means \&quot;UTC\&quot;. | [optional] 
 **use_filter_tz** | **str**| When passed as \&quot;true\&quot; the timezone from start_time_in or end_time_in will be used for all timestamps in the response. Otherwise they&#39;ll use UTC. | [optional] 
 **serializer_view** | **str**| Changes what fields are included in the response. | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner]**](RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_entries_id_change_history_get**
> List[TimecardEntryChangeHistory] rest_v10_companies_company_id_timecard_entries_id_change_history_get(procore_company_id, id, company_id)

Show timecard entry change history (Company)

Returns the change history for a Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.timecard_entry_change_history import TimecardEntryChangeHistory
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timecard entry change history (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_id_change_history_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_change_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_change_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[TimecardEntryChangeHistory]**](TimecardEntryChangeHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_entries_id_delete**
> RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner rest_v10_companies_company_id_timecard_entries_id_delete(procore_company_id, id, company_id)

Delete timecard entry (Company)

Detete a specific Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete timecard entry (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_id_delete(procore_company_id, id, company_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner**](RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_entries_id_get**
> RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner rest_v10_companies_company_id_timecard_entries_id_get(procore_company_id, id, company_id)

Show timecard entry (Company)

Return detailed information about a specific Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timecard entry (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner**](RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_entries_id_patch**
> RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner rest_v10_companies_company_id_timecard_entries_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_timecard_entries_id_patch_request)

Update timecard entry (Company)

Update a specified Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_id_patch_request import RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_timecard_entries_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest() # RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest | 

    try:
        # Update timecard entry (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_timecard_entries_id_patch_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_timecard_entries_id_patch_request** | [**RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest**](RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner**](RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_entries_post**
> RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner rest_v10_companies_company_id_timecard_entries_post(procore_company_id, company_id, rest_v10_companies_company_id_timecard_entries_post_request)

Create timecard entry (Company)

Create a new Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_post_request import RestV10CompaniesCompanyIdTimecardEntriesPostRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_timecard_entries_post_request = procore_sdk.RestV10CompaniesCompanyIdTimecardEntriesPostRequest() # RestV10CompaniesCompanyIdTimecardEntriesPostRequest | 

    try:
        # Create timecard entry (Company)
        api_response = api_instance.rest_v10_companies_company_id_timecard_entries_post(procore_company_id, company_id, rest_v10_companies_company_id_timecard_entries_post_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_companies_company_id_timecard_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_timecard_entries_post_request** | [**RestV10CompaniesCompanyIdTimecardEntriesPostRequest**](RestV10CompaniesCompanyIdTimecardEntriesPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner**](RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_get**
> List[RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner] rest_v10_projects_project_id_timecard_entries_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, page=page, per_page=per_page, filters_created_by_id=filters_created_by_id)

List timecard entries (Project)

Returns a list of all timecard entries for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Timecard entries at the specified date. (YYYY-MM-DD) (optional)
    start_date = '2013-10-20' # date | The beginning of the date range for timecard entries. (YYYY-MM-DD) Start date is inclusive. (optional)
    end_date = '2013-10-20' # date | The end of the date range for timecard entries. (YYYY-MM-DD) End date is inclusive. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)

    try:
        # List timecard entries (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, page=page, per_page=per_page, filters_created_by_id=filters_created_by_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Timecard entries at the specified date. (YYYY-MM-DD) | [optional] 
 **start_date** | **date**| The beginning of the date range for timecard entries. (YYYY-MM-DD) Start date is inclusive. | [optional] 
 **end_date** | **date**| The end of the date range for timecard entries. (YYYY-MM-DD) End date is inclusive. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner]**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_id_delete**
> rest_v10_projects_project_id_timecard_entries_id_delete(procore_company_id, project_id, id)

Delete timecard entry (Project)

Delete a specific timecard entry.

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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the timecard entry

    try:
        # Delete timecard entry (Project)
        api_instance.rest_v10_projects_project_id_timecard_entries_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the timecard entry | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_id_get**
> RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner rest_v10_projects_project_id_timecard_entries_id_get(procore_company_id, project_id, id)

Show timecard entry (Project)

Return detailed information about a specific timecard entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the timecard entry

    try:
        # Show timecard entry (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the timecard entry | 

### Return type

[**RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_id_patch**
> RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner rest_v10_projects_project_id_timecard_entries_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_timecard_entries_id_patch_request)

Update timecard entry (Project)

Update a specific timecard entry.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_id_patch_request import RestV10ProjectsProjectIdTimecardEntriesIdPatchRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the timecard entry
    rest_v10_projects_project_id_timecard_entries_id_patch_request = procore_sdk.RestV10ProjectsProjectIdTimecardEntriesIdPatchRequest() # RestV10ProjectsProjectIdTimecardEntriesIdPatchRequest | 

    try:
        # Update timecard entry (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_timecard_entries_id_patch_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the timecard entry | 
 **rest_v10_projects_project_id_timecard_entries_id_patch_request** | [**RestV10ProjectsProjectIdTimecardEntriesIdPatchRequest**](RestV10ProjectsProjectIdTimecardEntriesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch**
> RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch(procore_company_id, id, project_id)

Remove signature from timecard entry (Project)

Remove the signature ID from the provided timecard entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | The ID of the timecard entry.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Remove signature from timecard entry (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_remove_signature_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| The ID of the timecard entry. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timecard Entry |  -  |
**403** | User does not have permission to remove the signature from the provided timecard entry. |  -  |
**404** | The timecard entry could not be found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_id_sign_patch**
> RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner rest_v10_projects_project_id_timecard_entries_id_sign_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_timecard_entries_id_sign_patch_request)

Update timecard entry signature (Project)

Update timecard entry signature with the provided signature ID.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_id_sign_patch_request import RestV10ProjectsProjectIdTimecardEntriesIdSignPatchRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | The ID of the timecard entry.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_timecard_entries_id_sign_patch_request = procore_sdk.RestV10ProjectsProjectIdTimecardEntriesIdSignPatchRequest() # RestV10ProjectsProjectIdTimecardEntriesIdSignPatchRequest | 

    try:
        # Update timecard entry signature (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_id_sign_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_timecard_entries_id_sign_patch_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_sign_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_id_sign_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| The ID of the timecard entry. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_timecard_entries_id_sign_patch_request** | [**RestV10ProjectsProjectIdTimecardEntriesIdSignPatchRequest**](RestV10ProjectsProjectIdTimecardEntriesIdSignPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timecard Entry |  -  |
**400** | An improper signature ID was submitted or the signature ID was omitted. |  -  |
**403** | User does not have permission to sign the provided timecard entry. |  -  |
**404** | The timecard entry was not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_timecard_entries_post**
> RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner rest_v10_projects_project_id_timecard_entries_post(procore_company_id, project_id, rest_v10_projects_project_id_timecard_entries_post_request)

Create timecard entry (Project)

Create a new Timecard Entry.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_get200_response_inner import RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_timecard_entries_post_request import RestV10ProjectsProjectIdTimecardEntriesPostRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_timecard_entries_post_request = procore_sdk.RestV10ProjectsProjectIdTimecardEntriesPostRequest() # RestV10ProjectsProjectIdTimecardEntriesPostRequest | 

    try:
        # Create timecard entry (Project)
        api_response = api_instance.rest_v10_projects_project_id_timecard_entries_post(procore_company_id, project_id, rest_v10_projects_project_id_timecard_entries_post_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_projects_project_id_timecard_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_timecard_entries_post_request** | [**RestV10ProjectsProjectIdTimecardEntriesPostRequest**](RestV10ProjectsProjectIdTimecardEntriesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_timecard_entries_get**
> List[RestV10TimecardEntriesGet200ResponseInner] rest_v10_timecard_entries_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)

List timecard entries

Return a list of all Timecard Entries within a specified date range.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_timecard_entries_get200_response_inner import RestV10TimecardEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    start_date = '2013-10-20' # date | The beginning of the date range for entries. (YYYY-MM-DD) (optional)
    end_date = '2013-10-20' # date | The end of the date range for entries. (YYYY-MM-DD) (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List timecard entries
        api_response = api_instance.rest_v10_timecard_entries_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **start_date** | **date**| The beginning of the date range for entries. (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| The end of the date range for entries. (YYYY-MM-DD) | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10TimecardEntriesGet200ResponseInner]**](RestV10TimecardEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_timecard_entries_id_delete**
> rest_v10_timecard_entries_id_delete(procore_company_id, id, project_id)

Delete timecard entry

Detete a specific Timecard Entry.

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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete timecard entry
        api_instance.rest_v10_timecard_entries_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_timecard_entries_id_get**
> RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response rest_v10_timecard_entries_id_get(procore_company_id, id, project_id)

Show timecard entry

Return detailed information about a specific Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_project_timecard_entries_post200_response import RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show timecard entry
        api_response = api_instance.rest_v10_timecard_entries_id_get(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response**](RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_timecard_entries_id_patch**
> RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response rest_v10_timecard_entries_id_patch(procore_company_id, id, rest_v10_timecard_entries_post_request)

Update timecard entry

Update a specified Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_timecard_entries_post_request import RestV10TimecardEntriesPostRequest
from procore_sdk.models.rest_v11_projects_project_id_project_timecard_entries_post200_response import RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the timecard entry
    rest_v10_timecard_entries_post_request = procore_sdk.RestV10TimecardEntriesPostRequest() # RestV10TimecardEntriesPostRequest | 

    try:
        # Update timecard entry
        api_response = api_instance.rest_v10_timecard_entries_id_patch(procore_company_id, id, rest_v10_timecard_entries_post_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the timecard entry | 
 **rest_v10_timecard_entries_post_request** | [**RestV10TimecardEntriesPostRequest**](RestV10TimecardEntriesPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response**](RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_timecard_entries_post**
> RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response rest_v10_timecard_entries_post(procore_company_id, rest_v10_timecard_entries_post_request)

Create timecard entry

Create a new Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_timecard_entries_post_request import RestV10TimecardEntriesPostRequest
from procore_sdk.models.rest_v11_projects_project_id_project_timecard_entries_post200_response import RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response
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
    api_instance = procore_sdk.FieldProductivityTimecardTimecardEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_timecard_entries_post_request = procore_sdk.RestV10TimecardEntriesPostRequest() # RestV10TimecardEntriesPostRequest | 

    try:
        # Create timecard entry
        api_response = api_instance.rest_v10_timecard_entries_post(procore_company_id, rest_v10_timecard_entries_post_request)
        print("The response of FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardTimecardEntriesApi->rest_v10_timecard_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_timecard_entries_post_request** | [**RestV10TimecardEntriesPostRequest**](RestV10TimecardEntriesPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response**](RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

