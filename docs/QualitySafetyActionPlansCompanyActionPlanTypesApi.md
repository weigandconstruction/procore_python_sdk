# procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_action_plans_plan_types_get**](QualitySafetyActionPlansCompanyActionPlanTypesApi.md#rest_v10_companies_company_id_action_plans_plan_types_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/plan_types | List Company Action Plan Types
[**rest_v10_companies_company_id_action_plans_plan_types_id_delete**](QualitySafetyActionPlansCompanyActionPlanTypesApi.md#rest_v10_companies_company_id_action_plans_plan_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/action_plans/plan_types/{id} | Delete Company Action Plan Type
[**rest_v10_companies_company_id_action_plans_plan_types_id_get**](QualitySafetyActionPlansCompanyActionPlanTypesApi.md#rest_v10_companies_company_id_action_plans_plan_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/plan_types/{id} | Show Company Action Plan Type
[**rest_v10_companies_company_id_action_plans_plan_types_id_patch**](QualitySafetyActionPlansCompanyActionPlanTypesApi.md#rest_v10_companies_company_id_action_plans_plan_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/action_plans/plan_types/{id} | Update Company Action Plan Type
[**rest_v10_companies_company_id_action_plans_plan_types_post**](QualitySafetyActionPlansCompanyActionPlanTypesApi.md#rest_v10_companies_company_id_action_plans_plan_types_post) | **POST** /rest/v1.0/companies/{company_id}/action_plans/plan_types | Create a Company Action Plan Type


# **rest_v10_companies_company_id_action_plans_plan_types_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType] rest_v10_companies_company_id_action_plans_plan_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Company Action Plan Types

List of all Company Action Plan Types for a Company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Company Action Plan Types
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType]**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md)

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

# **rest_v10_companies_company_id_action_plans_plan_types_id_delete**
> rest_v10_companies_company_id_action_plans_plan_types_id_delete(procore_company_id, company_id, id)

Delete Company Action Plan Type

Delete an Company Action Plan Type

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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Action Plan Type ID

    try:
        # Delete Company Action Plan Type
        api_instance.rest_v10_companies_company_id_action_plans_plan_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Action Plan Type ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_action_plans_plan_types_id_get**
> RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType rest_v10_companies_company_id_action_plans_plan_types_id_get(procore_company_id, company_id, id)

Show Company Action Plan Type

Details of a Company Action Plan Type

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Action Plan Type ID

    try:
        # Show Company Action Plan Type
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_types_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Action Plan Type ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_action_plans_plan_types_id_patch**
> RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType rest_v10_companies_company_id_action_plans_plan_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_action_plans_plan_types_id_patch_request)

Update Company Action Plan Type

Update an Company Action Plan Type

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_types_id_patch_request import RestV10CompaniesCompanyIdActionPlansPlanTypesIdPatchRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Action Plan Type ID
    rest_v10_companies_company_id_action_plans_plan_types_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdActionPlansPlanTypesIdPatchRequest() # RestV10CompaniesCompanyIdActionPlansPlanTypesIdPatchRequest | 

    try:
        # Update Company Action Plan Type
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_action_plans_plan_types_id_patch_request)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Action Plan Type ID | 
 **rest_v10_companies_company_id_action_plans_plan_types_id_patch_request** | [**RestV10CompaniesCompanyIdActionPlansPlanTypesIdPatchRequest**](RestV10CompaniesCompanyIdActionPlansPlanTypesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_action_plans_plan_types_post**
> RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType rest_v10_companies_company_id_action_plans_plan_types_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_plan_types_post_request)

Create a Company Action Plan Type

Create a Company Action Plan Type for a Company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_types_post_request import RestV10CompaniesCompanyIdActionPlansPlanTypesPostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_action_plans_plan_types_post_request = procore_sdk.RestV10CompaniesCompanyIdActionPlansPlanTypesPostRequest() # RestV10CompaniesCompanyIdActionPlansPlanTypesPostRequest | 

    try:
        # Create a Company Action Plan Type
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_types_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_plan_types_post_request)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTypesApi->rest_v10_companies_company_id_action_plans_plan_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_action_plans_plan_types_post_request** | [**RestV10CompaniesCompanyIdActionPlansPlanTypesPostRequest**](RestV10CompaniesCompanyIdActionPlansPlanTypesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

