# procore_sdk.CoreCompanyDirectoryDistributionGroupsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_distribution_groups_get**](CoreCompanyDirectoryDistributionGroupsApi.md#rest_v10_companies_company_id_distribution_groups_get) | **GET** /rest/v1.0/companies/{company_id}/distribution_groups | List Distribution Groups


# **rest_v10_companies_company_id_distribution_groups_get**
> List[RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner] rest_v10_companies_company_id_distribution_groups_get(procore_company_id, company_id, page=page, per_page=per_page, filters_search=filters_search, with_domain_users=with_domain_users, sort=sort, view=view)

List Distribution Groups

Return a list of all Distribution Groups associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter import RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_get200_response_inner import RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryDistributionGroupsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    with_domain_users = procore_sdk.RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter() # RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter | Return list of user IDs that have permissions to view specified domain. (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)
    view = 'view_example' # str | Parameter affecting what level of detail will be returned from the endpoint. 'extended' will include the users included in each distribution group. (optional)

    try:
        # List Distribution Groups
        api_response = api_instance.rest_v10_companies_company_id_distribution_groups_get(procore_company_id, company_id, page=page, per_page=per_page, filters_search=filters_search, with_domain_users=with_domain_users, sort=sort, view=view)
        print("The response of CoreCompanyDirectoryDistributionGroupsApi->rest_v10_companies_company_id_distribution_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryDistributionGroupsApi->rest_v10_companies_company_id_distribution_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **with_domain_users** | [**RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter**](.md)| Return list of user IDs that have permissions to view specified domain. | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 
 **view** | **str**| Parameter affecting what level of detail will be returned from the endpoint. &#39;extended&#39; will include the users included in each distribution group. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner]**](RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner.md)

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

