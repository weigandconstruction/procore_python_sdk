# procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_action_plans_verification_methods_get**](QualitySafetyActionPlansActionPlanVerificationMethodsApi.md#rest_v10_companies_company_id_action_plans_verification_methods_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/verification_methods | List Action Plan Verification Methods
[**rest_v10_companies_company_id_action_plans_verification_methods_id_delete**](QualitySafetyActionPlansActionPlanVerificationMethodsApi.md#rest_v10_companies_company_id_action_plans_verification_methods_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/action_plans/verification_methods/{id} | Delete Action Plan Verification Method
[**rest_v10_companies_company_id_action_plans_verification_methods_id_get**](QualitySafetyActionPlansActionPlanVerificationMethodsApi.md#rest_v10_companies_company_id_action_plans_verification_methods_id_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/verification_methods/{id} | Show Action Plan Verification Method
[**rest_v10_companies_company_id_action_plans_verification_methods_id_patch**](QualitySafetyActionPlansActionPlanVerificationMethodsApi.md#rest_v10_companies_company_id_action_plans_verification_methods_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/action_plans/verification_methods/{id} | Update Action Plan Verification Method
[**rest_v10_companies_company_id_action_plans_verification_methods_post**](QualitySafetyActionPlansActionPlanVerificationMethodsApi.md#rest_v10_companies_company_id_action_plans_verification_methods_post) | **POST** /rest/v1.0/companies/{company_id}/action_plans/verification_methods | Create Action Plan Verification Methods


# **rest_v10_companies_company_id_action_plans_verification_methods_get**
> List[RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner] rest_v10_companies_company_id_action_plans_verification_methods_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Action Plan Verification Methods

List of all company Action Plan Verification Methods

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner import RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi(api_client)
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
        # List Action Plan Verification Methods
        api_response = api_instance.rest_v10_companies_company_id_action_plans_verification_methods_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_get: %s\n" % e)
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

[**List[RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner]**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_action_plans_verification_methods_id_delete**
> rest_v10_companies_company_id_action_plans_verification_methods_id_delete(procore_company_id, company_id, id)

Delete Action Plan Verification Method

Delete an Action Plan Verification Method

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Action Plan Verification Method ID

    try:
        # Delete Action Plan Verification Method
        api_instance.rest_v10_companies_company_id_action_plans_verification_methods_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Action Plan Verification Method ID | 

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

# **rest_v10_companies_company_id_action_plans_verification_methods_id_get**
> RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner rest_v10_companies_company_id_action_plans_verification_methods_id_get(procore_company_id, company_id, id)

Show Action Plan Verification Method

Details of an Action Plan Verification Method

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner import RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Action Plan Verification Method ID

    try:
        # Show Action Plan Verification Method
        api_response = api_instance.rest_v10_companies_company_id_action_plans_verification_methods_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Action Plan Verification Method ID | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_action_plans_verification_methods_id_patch**
> RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner rest_v10_companies_company_id_action_plans_verification_methods_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_action_plans_verification_methods_id_patch_request)

Update Action Plan Verification Method

Update a company Action Plan Verification Method

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner import RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_id_patch_request import RestV10CompaniesCompanyIdActionPlansVerificationMethodsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Action Plan Verification Method ID
    rest_v10_companies_company_id_action_plans_verification_methods_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdActionPlansVerificationMethodsIdPatchRequest() # RestV10CompaniesCompanyIdActionPlansVerificationMethodsIdPatchRequest | 

    try:
        # Update Action Plan Verification Method
        api_response = api_instance.rest_v10_companies_company_id_action_plans_verification_methods_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_action_plans_verification_methods_id_patch_request)
        print("The response of QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Action Plan Verification Method ID | 
 **rest_v10_companies_company_id_action_plans_verification_methods_id_patch_request** | [**RestV10CompaniesCompanyIdActionPlansVerificationMethodsIdPatchRequest**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsIdPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_action_plans_verification_methods_post**
> RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner rest_v10_companies_company_id_action_plans_verification_methods_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_verification_methods_post_request)

Create Action Plan Verification Methods

Create an Action Plan Verification Method for a specified company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner import RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_post_request import RestV10CompaniesCompanyIdActionPlansVerificationMethodsPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanVerificationMethodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_action_plans_verification_methods_post_request = procore_sdk.RestV10CompaniesCompanyIdActionPlansVerificationMethodsPostRequest() # RestV10CompaniesCompanyIdActionPlansVerificationMethodsPostRequest | 

    try:
        # Create Action Plan Verification Methods
        api_response = api_instance.rest_v10_companies_company_id_action_plans_verification_methods_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_verification_methods_post_request)
        print("The response of QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanVerificationMethodsApi->rest_v10_companies_company_id_action_plans_verification_methods_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_action_plans_verification_methods_post_request** | [**RestV10CompaniesCompanyIdActionPlansVerificationMethodsPostRequest**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner**](RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.md)

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

