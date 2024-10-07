# procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post**](QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi.md#rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post) | **POST** /rest/v1.0/companies/{company_id}/action_plans/plan_template_sections/create_from_section | Create a copy of the Action Plan Template Section in the Section&#39;s Template.
[**rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get**](QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi.md#rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/action_plans/plan_template_sections | List Recycled Action Plan Template Sections
[**rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get**](QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi.md#rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/action_plans/plan_template_sections/{id} | Show Recycled Action Plan Template Section


# **rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post**
> RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post(procore_company_id, company_id, rest_v10_projects_project_id_action_plans_plan_template_sections_create_from_section_post_request)

Create a copy of the Action Plan Template Section in the Section's Template.

Create a copy of the Action Plan Template Section in the Section's Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response import RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_sections_create_from_section_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateSectionsCreateFromSectionPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_projects_project_id_action_plans_plan_template_sections_create_from_section_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateSectionsCreateFromSectionPostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateSectionsCreateFromSectionPostRequest | 

    try:
        # Create a copy of the Action Plan Template Section in the Section's Template.
        api_response = api_instance.rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post(procore_company_id, company_id, rest_v10_projects_project_id_action_plans_plan_template_sections_create_from_section_post_request)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_projects_project_id_action_plans_plan_template_sections_create_from_section_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateSectionsCreateFromSectionPostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateSectionsCreateFromSectionPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response**](RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get**
> List[RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner] rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)

List Recycled Action Plan Template Sections

Returns all Recycled Action Plan Template Sections for a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Action Plan Template Sections
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get(procore_company_id, company_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get: %s\n" % e)
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
 **filters_plan_template_id** | [**List[int]**](int.md)| Return section(s) associated with the specified Action Plan Template ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner]**](RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get**
> RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get(procore_company_id, company_id, id)

Show Recycled Action Plan Template Section

Returns a Recycled Action Plan Template Section

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Action Plan Template Section ID

    try:
        # Show Recycled Action Plan Template Section
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansCompanyActionPlanTemplateSectionsApi->rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Action Plan Template Section ID | 

### Return type

[**RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner**](RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner.md)

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

