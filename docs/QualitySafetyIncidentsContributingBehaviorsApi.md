# procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/contributing_behaviors/bulk_update | Bulk Update Contributing Behaviors
[**rest_v10_companies_company_id_contributing_behaviors_get**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_get) | **GET** /rest/v1.0/companies/{company_id}/contributing_behaviors | List Contributing Behaviors
[**rest_v10_companies_company_id_contributing_behaviors_id_delete**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/contributing_behaviors/{id} | Delete Contributing Behavior
[**rest_v10_companies_company_id_contributing_behaviors_id_get**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_id_get) | **GET** /rest/v1.0/companies/{company_id}/contributing_behaviors/{id} | Show Contributing Behavior
[**rest_v10_companies_company_id_contributing_behaviors_id_patch**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/contributing_behaviors/{id} | Update Contributing Behavior
[**rest_v10_companies_company_id_contributing_behaviors_post**](QualitySafetyIncidentsContributingBehaviorsApi.md#rest_v10_companies_company_id_contributing_behaviors_post) | **POST** /rest/v1.0/companies/{company_id}/contributing_behaviors | Create Contributing Behavior


# **rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch**
> List[ContributingBehavior1] rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request)

Bulk Update Contributing Behaviors

Update multiple Contributing Behaviors with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1
from procore_sdk.models.rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request import RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequest | 

    try:
        # Bulk Update Contributing Behaviors
        api_response = api_instance.rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_contributing_behaviors_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdContributingBehaviorsBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[ContributingBehavior1]**](ContributingBehavior1.md)

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

# **rest_v10_companies_company_id_contributing_behaviors_get**
> List[ContributingBehavior1] rest_v10_companies_company_id_contributing_behaviors_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)

List Contributing Behaviors

Return a list of all active Contributing Behaviors associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    all = True # bool | Both active and inactive Contributing Behaviors (optional)

    try:
        # List Contributing Behaviors
        api_response = api_instance.rest_v10_companies_company_id_contributing_behaviors_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)
        print("The response of QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_get: %s\n" % e)
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
 **all** | **bool**| Both active and inactive Contributing Behaviors | [optional] 

### Return type

[**List[ContributingBehavior1]**](ContributingBehavior1.md)

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

# **rest_v10_companies_company_id_contributing_behaviors_id_delete**
> rest_v10_companies_company_id_contributing_behaviors_id_delete(procore_company_id, company_id, id)

Delete Contributing Behavior

Deletes a Contributing Behavior. Note that Procore provided Contributing Behaviors cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Behavior ID

    try:
        # Delete Contributing Behavior
        api_instance.rest_v10_companies_company_id_contributing_behaviors_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Behavior ID | 

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

# **rest_v10_companies_company_id_contributing_behaviors_id_get**
> ContributingBehavior1 rest_v10_companies_company_id_contributing_behaviors_id_get(procore_company_id, company_id, id)

Show Contributing Behavior

Returns the details for a specified Contributing Behavior.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Behavior ID

    try:
        # Show Contributing Behavior
        api_response = api_instance.rest_v10_companies_company_id_contributing_behaviors_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Behavior ID | 

### Return type

[**ContributingBehavior1**](ContributingBehavior1.md)

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

# **rest_v10_companies_company_id_contributing_behaviors_id_patch**
> ContributingBehavior1 rest_v10_companies_company_id_contributing_behaviors_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_contributing_behaviors_id_patch_request)

Update Contributing Behavior

Updates a Contributing Behavior. Note that Procore provided Contributing Behaviors' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1
from procore_sdk.models.rest_v10_companies_company_id_contributing_behaviors_id_patch_request import RestV10CompaniesCompanyIdContributingBehaviorsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Contributing Behavior ID
    rest_v10_companies_company_id_contributing_behaviors_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdContributingBehaviorsIdPatchRequest() # RestV10CompaniesCompanyIdContributingBehaviorsIdPatchRequest | 

    try:
        # Update Contributing Behavior
        api_response = api_instance.rest_v10_companies_company_id_contributing_behaviors_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_contributing_behaviors_id_patch_request)
        print("The response of QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Contributing Behavior ID | 
 **rest_v10_companies_company_id_contributing_behaviors_id_patch_request** | [**RestV10CompaniesCompanyIdContributingBehaviorsIdPatchRequest**](RestV10CompaniesCompanyIdContributingBehaviorsIdPatchRequest.md)|  | 

### Return type

[**ContributingBehavior1**](ContributingBehavior1.md)

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

# **rest_v10_companies_company_id_contributing_behaviors_post**
> ContributingBehavior1 rest_v10_companies_company_id_contributing_behaviors_post(procore_company_id, company_id, rest_v10_companies_company_id_contributing_behaviors_post_request)

Create Contributing Behavior

Creates a Contributing Behavior with the specified name.

### Example


```python
import procore_sdk
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1
from procore_sdk.models.rest_v10_companies_company_id_contributing_behaviors_post_request import RestV10CompaniesCompanyIdContributingBehaviorsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsContributingBehaviorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_contributing_behaviors_post_request = procore_sdk.RestV10CompaniesCompanyIdContributingBehaviorsPostRequest() # RestV10CompaniesCompanyIdContributingBehaviorsPostRequest | 

    try:
        # Create Contributing Behavior
        api_response = api_instance.rest_v10_companies_company_id_contributing_behaviors_post(procore_company_id, company_id, rest_v10_companies_company_id_contributing_behaviors_post_request)
        print("The response of QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsContributingBehaviorsApi->rest_v10_companies_company_id_contributing_behaviors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_contributing_behaviors_post_request** | [**RestV10CompaniesCompanyIdContributingBehaviorsPostRequest**](RestV10CompaniesCompanyIdContributingBehaviorsPostRequest.md)|  | 

### Return type

[**ContributingBehavior1**](ContributingBehavior1.md)

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

