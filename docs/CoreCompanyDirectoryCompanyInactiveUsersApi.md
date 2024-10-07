# procore_sdk.CoreCompanyDirectoryCompanyInactiveUsersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_users_inactive_get**](CoreCompanyDirectoryCompanyInactiveUsersApi.md#rest_v10_companies_company_id_users_inactive_get) | **GET** /rest/v1.0/companies/{company_id}/users/inactive | List company inactive users
[**rest_v10_companies_company_id_users_inactive_id_patch**](CoreCompanyDirectoryCompanyInactiveUsersApi.md#rest_v10_companies_company_id_users_inactive_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/users/inactive/{id} | Reactivate company user


# **rest_v10_companies_company_id_users_inactive_get**
> List[InactiveUser] rest_v10_companies_company_id_users_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, sort=sort)

List company inactive users

Return a list of all Inactive Users associated with a Company.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.inactive_user import InactiveUser
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyInactiveUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List company inactive users
        api_response = api_instance.rest_v10_companies_company_id_users_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, sort=sort)
        print("The response of CoreCompanyDirectoryCompanyInactiveUsersApi->rest_v10_companies_company_id_users_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyInactiveUsersApi->rest_v10_companies_company_id_users_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[InactiveUser]**](InactiveUser.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_users_inactive_id_patch**
> CompanyUser7 rest_v10_companies_company_id_users_inactive_id_patch(procore_company_id, company_id, id)

Reactivate company user

Reactivate the specified User.

### Example


```python
import procore_sdk
from procore_sdk.models.company_user7 import CompanyUser7
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyInactiveUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the user

    try:
        # Reactivate company user
        api_response = api_instance.rest_v10_companies_company_id_users_inactive_id_patch(procore_company_id, company_id, id)
        print("The response of CoreCompanyDirectoryCompanyInactiveUsersApi->rest_v10_companies_company_id_users_inactive_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyInactiveUsersApi->rest_v10_companies_company_id_users_inactive_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the user | 

### Return type

[**CompanyUser7**](CompanyUser7.md)

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

