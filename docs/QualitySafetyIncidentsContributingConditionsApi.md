# procore_sdk.QualitySafetyIncidentsContributingConditionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_contributing_conditions_bulk_update_patch**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/contributing_conditions/bulk_update | Bulk Update Contributing Conditions
[**rest_v10_companies_company_id_contributing_conditions_get**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_get) | **GET** /rest/v1.0/companies/{company_id}/contributing_conditions | List Contributing Conditions
[**rest_v10_companies_company_id_contributing_conditions_id_delete**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/contributing_conditions/{id} | Delete Contributing Condition
[**rest_v10_companies_company_id_contributing_conditions_id_get**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_id_get) | **GET** /rest/v1.0/companies/{company_id}/contributing_conditions/{id} | Show Contributing Condition
[**rest_v10_companies_company_id_contributing_conditions_id_patch**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/contributing_conditions/{id} | Update Contributing Condition
[**rest_v10_companies_company_id_contributing_conditions_post**](QualitySafetyIncidentsContributingConditionsApi.md#rest_v10_companies_company_id_contributing_conditions_post) | **POST** /rest/v1.0/companies/{company_id}/contributing_conditions | Create Contributing Condition


# **rest_v10_companies_company_id_contributing_conditions_bulk_update_patch**
> List[ContributingCondition1] rest_v10_companies_company_id_contributing_conditions_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request)

Bulk Update Contributing Conditions

Update multiple Contributing Conditions with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_condition1 import ContributingCondition1
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request import RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequest | 

    try:
        # Bulk Update Contributing Conditions
        api_response = api_instance.rest_v10_companies_company_id_contributing_conditions_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_contributing_conditions_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdContributingConditionsBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[ContributingCondition1]**](ContributingCondition1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_contributing_conditions_get**
> List[ContributingCondition1] rest_v10_companies_company_id_contributing_conditions_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)

List Contributing Conditions

Return a list of all active Contributing Conditions associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_condition1 import ContributingCondition1
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    all = True # bool | Both active and inactive Contributing Conditions (optional)

    try:
        # List Contributing Conditions
        api_response = api_instance.rest_v10_companies_company_id_contributing_conditions_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)
        print("The response of QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **all** | **bool**| Both active and inactive Contributing Conditions | [optional] 

### Return type

[**List[ContributingCondition1]**](ContributingCondition1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_contributing_conditions_id_delete**
> rest_v10_companies_company_id_contributing_conditions_id_delete(procore_company_id, company_id, id)

Delete Contributing Condition

Deletes a Contributing Condition. Note that Procore provided Contributing Conditions cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Condition ID

    try:
        # Delete Contributing Condition
        api_instance.rest_v10_companies_company_id_contributing_conditions_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Condition ID | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_contributing_conditions_id_get**
> ContributingCondition1 rest_v10_companies_company_id_contributing_conditions_id_get(procore_company_id, company_id, id)

Show Contributing Condition

Returns the details for a specified Contributing Condition.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_condition1 import ContributingCondition1
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Condition ID

    try:
        # Show Contributing Condition
        api_response = api_instance.rest_v10_companies_company_id_contributing_conditions_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Condition ID | 

### Return type

[**ContributingCondition1**](ContributingCondition1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_contributing_conditions_id_patch**
> ContributingCondition1 rest_v10_companies_company_id_contributing_conditions_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_contributing_conditions_id_patch_request)

Update Contributing Condition

Updates a Contributing Condition. Note that Procore provided Contributing Conditions' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_condition1 import ContributingCondition1
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_id_patch_request import RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Condition ID
    rest_v10_companies_company_id_contributing_conditions_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest() # RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest | 

    try:
        # Update Contributing Condition
        api_response = api_instance.rest_v10_companies_company_id_contributing_conditions_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_contributing_conditions_id_patch_request)
        print("The response of QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Condition ID | 
 **rest_v10_companies_company_id_contributing_conditions_id_patch_request** | [**RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest**](RestV10CompaniesCompanyIdContributingConditionsIdPatchRequest.md)|  | 

### Return type

[**ContributingCondition1**](ContributingCondition1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_contributing_conditions_post**
> ContributingCondition1 rest_v10_companies_company_id_contributing_conditions_post(procore_company_id, company_id, rest_v10_companies_company_id_contributing_conditions_post_request)

Create Contributing Condition

Creates a Contributing Condition with the specified name.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_condition1 import ContributingCondition1
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_post_request import RestV10CompaniesCompanyIdContributingConditionsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_contributing_conditions_post_request = procore_sdk.RestV10CompaniesCompanyIdContributingConditionsPostRequest() # RestV10CompaniesCompanyIdContributingConditionsPostRequest | 

    try:
        # Create Contributing Condition
        api_response = api_instance.rest_v10_companies_company_id_contributing_conditions_post(procore_company_id, company_id, rest_v10_companies_company_id_contributing_conditions_post_request)
        print("The response of QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingConditionsApi->rest_v10_companies_company_id_contributing_conditions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_contributing_conditions_post_request** | [**RestV10CompaniesCompanyIdContributingConditionsPostRequest**](RestV10CompaniesCompanyIdContributingConditionsPostRequest.md)|  | 

### Return type

[**ContributingCondition1**](ContributingCondition1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

