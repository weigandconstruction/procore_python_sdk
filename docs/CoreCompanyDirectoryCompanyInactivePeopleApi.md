# procore_sdk.CoreCompanyDirectoryCompanyInactivePeopleApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_people_inactive_get**](CoreCompanyDirectoryCompanyInactivePeopleApi.md#rest_v10_companies_company_id_people_inactive_get) | **GET** /rest/v1.0/companies/{company_id}/people/inactive | List Inactive Company People


# **rest_v10_companies_company_id_people_inactive_get**
> List[CompanyPerson] rest_v10_companies_company_id_people_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, filters_is_employee=filters_is_employee, filters_reference_users_only=filters_reference_users_only, filters_include_company_people=filters_include_company_people, filters_search=filters_search)

List Inactive Company People

Return a list of People associated with a Company. Includes users in the directory and reference users. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.company_person import CompanyPerson
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyInactivePeopleApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | ID of the project
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_is_employee = True # bool | If true, returns item(s) where `is_employee` value is true. (optional)
    filters_reference_users_only = True # bool | If true, returns only people who are reference users. (optional)
    filters_include_company_people = True # bool | If true, returns people in the Company not just the Project. This option only works if the user has permission to create people in the project directory or permission to read from the company directory. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)

    try:
        # List Inactive Company People
        api_response = api_instance.rest_v10_companies_company_id_people_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, filters_is_employee=filters_is_employee, filters_reference_users_only=filters_reference_users_only, filters_include_company_people=filters_include_company_people, filters_search=filters_search)
        print("The response of CoreCompanyDirectoryCompanyInactivePeopleApi->rest_v10_companies_company_id_people_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyInactivePeopleApi->rest_v10_companies_company_id_people_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| ID of the project | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_is_employee** | **bool**| If true, returns item(s) where &#x60;is_employee&#x60; value is true. | [optional] 
 **filters_reference_users_only** | **bool**| If true, returns only people who are reference users. | [optional] 
 **filters_include_company_people** | **bool**| If true, returns people in the Company not just the Project. This option only works if the user has permission to create people in the project directory or permission to read from the company directory. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 

### Return type

[**List[CompanyPerson]**](CompanyPerson.md)

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

