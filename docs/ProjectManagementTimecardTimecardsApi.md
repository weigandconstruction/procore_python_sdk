# procore_sdk.ProjectManagementTimecardTimecardsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_timecard_time_types_get**](ProjectManagementTimecardTimecardsApi.md#rest_v10_companies_company_id_timecard_time_types_get) | **GET** /rest/v1.0/companies/{company_id}/timecard_time_types | List Timecard Time Types
[**rest_v10_companies_company_id_timecard_time_types_id_patch**](ProjectManagementTimecardTimecardsApi.md#rest_v10_companies_company_id_timecard_time_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/timecard_time_types/{id} | Update Timecard Time Type


# **rest_v10_companies_company_id_timecard_time_types_get**
> List[TimecardTimeType4] rest_v10_companies_company_id_timecard_time_types_get(procore_company_id, company_id)

List Timecard Time Types

Return a list of all Timecard Time Types for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.timecard_time_type4 import TimecardTimeType4
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
    api_instance = procore_sdk.ProjectManagementTimecardTimecardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List Timecard Time Types
        api_response = api_instance.rest_v10_companies_company_id_timecard_time_types_get(procore_company_id, company_id)
        print("The response of ProjectManagementTimecardTimecardsApi->rest_v10_companies_company_id_timecard_time_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementTimecardTimecardsApi->rest_v10_companies_company_id_timecard_time_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[TimecardTimeType4]**](TimecardTimeType4.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timecard_time_types_id_patch**
> TimecardTimeType4 rest_v10_companies_company_id_timecard_time_types_id_patch(procore_company_id, company_id, id, timecard_time_type_body)

Update Timecard Time Type

Return an update Timecard Time Type for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.timecard_time_type4 import TimecardTimeType4
from procore_sdk.models.timecard_time_type_body import TimecardTimeTypeBody
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
    api_instance = procore_sdk.ProjectManagementTimecardTimecardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Timecard Time Type
    timecard_time_type_body = procore_sdk.TimecardTimeTypeBody() # TimecardTimeTypeBody | 

    try:
        # Update Timecard Time Type
        api_response = api_instance.rest_v10_companies_company_id_timecard_time_types_id_patch(procore_company_id, company_id, id, timecard_time_type_body)
        print("The response of ProjectManagementTimecardTimecardsApi->rest_v10_companies_company_id_timecard_time_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementTimecardTimecardsApi->rest_v10_companies_company_id_timecard_time_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Timecard Time Type | 
 **timecard_time_type_body** | [**TimecardTimeTypeBody**](TimecardTimeTypeBody.md)|  | 

### Return type

[**TimecardTimeType4**](TimecardTimeType4.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timecard Time Type updated |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a Timecard Time Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

