# procore_sdk.ProjectManagementMeetingsMeetingTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_meeting_templates_get**](ProjectManagementMeetingsMeetingTemplatesApi.md#rest_v10_companies_company_id_meeting_templates_get) | **GET** /rest/v1.0/companies/{company_id}/meeting_templates | List Meeting Templates
[**rest_v10_companies_company_id_meeting_templates_id_get**](ProjectManagementMeetingsMeetingTemplatesApi.md#rest_v10_companies_company_id_meeting_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/meeting_templates/{id} | Show a Meeting Template


# **rest_v10_companies_company_id_meeting_templates_get**
> List[RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner] rest_v10_companies_company_id_meeting_templates_get(procore_company_id, company_id, page=page, per_page=per_page)

List Meeting Templates

Returns all templates for a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_meeting_templates_get200_response_inner import RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Meeting Templates
        api_response = api_instance.rest_v10_companies_company_id_meeting_templates_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of ProjectManagementMeetingsMeetingTemplatesApi->rest_v10_companies_company_id_meeting_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTemplatesApi->rest_v10_companies_company_id_meeting_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner]**](RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**404** | Endpoint not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_meeting_templates_id_get**
> RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner rest_v10_companies_company_id_meeting_templates_id_get(procore_company_id, company_id, id)

Show a Meeting Template

Returns a specific meeting template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_meeting_templates_get200_response_inner import RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Meeting Template ID

    try:
        # Show a Meeting Template
        api_response = api_instance.rest_v10_companies_company_id_meeting_templates_id_get(procore_company_id, company_id, id)
        print("The response of ProjectManagementMeetingsMeetingTemplatesApi->rest_v10_companies_company_id_meeting_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTemplatesApi->rest_v10_companies_company_id_meeting_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Meeting Template ID | 

### Return type

[**RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner**](RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**404** | Meeting Template not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

