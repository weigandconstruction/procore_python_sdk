# procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post) | **POST** /rest/v1.0/companies/{company_id}/action_plans/plan_template_references/bulk_create | Bulk Create Plan Template References
[**rest_v10_companies_company_id_action_plans_plan_template_references_get**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_action_plans_plan_template_references_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/plan_template_references | List Company Action Plan Template References
[**rest_v10_companies_company_id_action_plans_plan_template_references_id_delete**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_action_plans_plan_template_references_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/action_plans/plan_template_references/{id} | Delete Company Action Plan Template Reference
[**rest_v10_companies_company_id_action_plans_plan_template_references_id_get**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_action_plans_plan_template_references_id_get) | **GET** /rest/v1.0/companies/{company_id}/action_plans/plan_template_references/{id} | Show Company Action Plan Template Reference
[**rest_v10_companies_company_id_action_plans_plan_template_references_post**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_action_plans_plan_template_references_post) | **POST** /rest/v1.0/companies/{company_id}/action_plans/plan_template_references | Create Company Action Plan Template Reference
[**rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/action_plans/plan_template_references | List Recycled Company Action Plan Template References
[**rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get**](QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi.md#rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/action_plans/plan_template_references/{id} | Show Recycled Company Action Plan Template Reference


# **rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]] rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post_request, completion_mode=completion_mode)

Bulk Create Plan Template References

Creates multiple Plan Template References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post_request import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesBulkCreatePostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post_request = procore_sdk.RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesBulkCreatePostRequest() # RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesBulkCreatePostRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Create Plan Template References
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post(procore_company_id, company_id, rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_action_plans_plan_template_references_bulk_create_post_request** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesBulkCreatePostRequest**](RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesBulkCreatePostRequest.md)|  | 
 **completion_mode** | **str**| Whether to update what can be or nothing if one can not be updated. Defaults to \&quot;all_or_nothing\&quot; | [optional] 

### Return type

**List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]]**

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_action_plans_plan_template_references_get**
> List[RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner] rest_v10_companies_company_id_action_plans_plan_template_references_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_template_item_id=filters_plan_template_item_id, filters_plan_template_id=filters_plan_template_id, sort=sort)

List Company Action Plan Template References

List of all Company Action Plan Template References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_plan_template_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Template Item ID(s). (optional)
    filters_plan_template_id = 56 # int | Return item(s) associated with the specified Action Plan Template ID. (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Company Action Plan Template References
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_template_references_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_template_item_id=filters_plan_template_item_id, filters_plan_template_id=filters_plan_template_id, sort=sort)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_plan_template_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Template Item ID(s). | [optional] 
 **filters_plan_template_id** | **int**| Return item(s) associated with the specified Action Plan Template ID. | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner]**](RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_action_plans_plan_template_references_id_delete**
> rest_v10_companies_company_id_action_plans_plan_template_references_id_delete(procore_company_id, company_id, id)

Delete Company Action Plan Template Reference

Deletes a Company Action Plan Template Reference

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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Reference ID

    try:
        # Delete Company Action Plan Template Reference
        api_instance.rest_v10_companies_company_id_action_plans_plan_template_references_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Reference ID | 

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

# **rest_v10_companies_company_id_action_plans_plan_template_references_id_get**
> RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner rest_v10_companies_company_id_action_plans_plan_template_references_id_get(procore_company_id, company_id, id)

Show Company Action Plan Template Reference

Returns a Company Action Plan Template Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Reference ID

    try:
        # Show Company Action Plan Template Reference
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_template_references_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Reference ID | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner**](RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_action_plans_plan_template_references_post**
> RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner rest_v10_companies_company_id_action_plans_plan_template_references_post(procore_company_id, company_id, plan_template_reference)

Create Company Action Plan Template Reference

Create a Company Action Plan Template Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    plan_template_reference = procore_sdk.RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference() # RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference | 

    try:
        # Create Company Action Plan Template Reference
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_template_references_post(procore_company_id, company_id, plan_template_reference)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_action_plans_plan_template_references_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **plan_template_reference** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference**](RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner**](RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get**
> List[RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner] rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_template_item_id=filters_plan_template_item_id, filters_plan_template_id=filters_plan_template_id, sort=sort)

List Recycled Company Action Plan Template References

List of all Recycled Company Action Plan Template References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_plan_template_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Template Item ID(s). (optional)
    filters_plan_template_id = 56 # int | Return item(s) associated with the specified Action Plan Template ID. (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Recycled Company Action Plan Template References
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_template_item_id=filters_plan_template_item_id, filters_plan_template_id=filters_plan_template_id, sort=sort)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_plan_template_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Template Item ID(s). | [optional] 
 **filters_plan_template_id** | **int**| Return item(s) associated with the specified Action Plan Template ID. | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner]**](RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get**
> RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get(procore_company_id, company_id, id)

Show Recycled Company Action Plan Template Reference

Returns a Recycled Company Action Plan Template Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Action Plan Template Reference ID

    try:
        # Show Recycled Company Action Plan Template Reference
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateReferencesApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Action Plan Template Reference ID | 

### Return type

[**RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner**](RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner.md)

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

