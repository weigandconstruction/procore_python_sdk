# procore_sdk.ProjectManagementBiddingBidFormsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id}/bid_leveling | Bid Level across a Bid Form
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id} | Delete Bid Form
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id} | View Bid Form
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id} | Update Bid Form
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms | Index Bid Forms
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post**](ProjectManagementBiddingBidFormsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post) | **POST** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms | Create a Bid Form
[**rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get**](ProjectManagementBiddingBidFormsApi.md#rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get) | **GET** /rest/v1.1/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id}/bid_leveling | Bid Level across a Bid Form
[**rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch**](ProjectManagementBiddingBidFormsApi.md#rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms/{bid_form_id} | Update Bid Form
[**rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post**](ProjectManagementBiddingBidFormsApi.md#rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post) | **POST** /rest/v1.1/projects/{project_id}/bid_packages/{bid_package_id}/bid_forms | Create a Bid Form


# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get**
> RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get(procore_company_id, project_id, bid_package_id, bid_form_id, export_format=export_format)

Bid Level across a Bid Form

Compare all bids submitted to a bid form

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID
    export_format = 'export_format_example' # str | Export File Format (optional)

    try:
        # Bid Level across a Bid Form
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get(procore_company_id, project_id, bid_package_id, bid_form_id, export_format=export_format)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 
 **export_format** | **str**| Export File Format | [optional] 

### Return type

[**RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response**](RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete**
> rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete(procore_company_id, project_id, bid_package_id, bid_form_id)

Delete Bid Form

Delete a single Bid Form and its associated Sections and Items.

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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID

    try:
        # Delete Bid Form
        api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete(procore_company_id, project_id, bid_package_id, bid_form_id)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 

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
**204** | No content |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form to delete |  -  |
**422** | Can not delete due to errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get(procore_company_id, project_id, bid_package_id, bid_form_id)

View Bid Form

View single Bid Form.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID

    try:
        # View Bid Form
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get(procore_company_id, project_id, bid_package_id, bid_form_id)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch(procore_company_id, project_id, bid_package_id, bid_form_id, body145)

Update Bid Form

Update single Bid Form.

### Example


```python
import procore_sdk
from procore_sdk.models.body145 import Body145
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID
    body145 = procore_sdk.Body145() # Body145 | 

    try:
        # Update Bid Form
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch(procore_company_id, project_id, bid_package_id, bid_form_id, body145)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 
 **body145** | [**Body145**](Body145.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form to update |  -  |
**422** | Can not update due to errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get**
> List[RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsGet200ResponseInner] rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get(procore_company_id, project_id, bid_package_id, excluded_bid_form_id=excluded_bid_form_id, view=view, search=search, sort=sort)

Index Bid Forms

Fetches a list of Bid Forms for a Bid Package

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get200_response_inner import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    excluded_bid_form_id = 56 # int | Bid Form Id to exclude (optional)
    view = 'view_example' # str | View that enables Use Previous Bidders functionality and provides project and bid package name (optional)
    search = 'search_example' # str | Search for a bid form (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # Index Bid Forms
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get(procore_company_id, project_id, bid_package_id, excluded_bid_form_id=excluded_bid_form_id, view=view, search=search, sort=sort)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **excluded_bid_form_id** | **int**| Bid Form Id to exclude | [optional] 
 **view** | **str**| View that enables Use Previous Bidders functionality and provides project and bid package name | [optional] 
 **search** | **str**| Search for a bid form | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsGet200ResponseInner]**](RestV10ProjectsProjectIdBidPackagesBidPackageIdBidFormsGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post(procore_company_id, project_id, bid_package_id, body145)

Create a Bid Form

Create a Bid Form for a Bid Package. A bid form is needed to submit a bid, since the bid will be made against the bid form.

### Example


```python
import procore_sdk
from procore_sdk.models.body145 import Body145
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    body145 = procore_sdk.Body145() # Body145 | 

    try:
        # Create a Bid Form
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post(procore_company_id, project_id, bid_package_id, body145)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bid_forms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **body145** | [**Body145**](Body145.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have right permissions |  -  |
**422** | Can not create due to errors |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get**
> RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get(procore_company_id, project_id, bid_package_id, bid_form_id, export_format=export_format)

Bid Level across a Bid Form

Compare all bids submitted to a bid form

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get200_response import RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID
    export_format = 'export_format_example' # str | Export File Format (optional)

    try:
        # Bid Level across a Bid Form
        api_response = api_instance.rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get(procore_company_id, project_id, bid_package_id, bid_form_id, export_format=export_format)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_bid_leveling_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 
 **export_format** | **str**| Export File Format | [optional] 

### Return type

[**RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response**](RestV11ProjectsProjectIdBidPackagesBidPackageIdBidFormsBidFormIdBidLevelingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have sufficient permission |  -  |
**404** | Cannot find bid form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch(procore_company_id, project_id, bid_package_id, bid_form_id, body144)

Update Bid Form

Update single Bid Form.

### Example


```python
import procore_sdk
from procore_sdk.models.body144 import Body144
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    bid_form_id = 56 # int | Bid Form ID
    body144 = procore_sdk.Body144() # Body144 | 

    try:
        # Update Bid Form
        api_response = api_instance.rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch(procore_company_id, project_id, bid_package_id, bid_form_id, body144)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_bid_form_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **bid_form_id** | **int**| Bid Form ID | 
 **body144** | [**Body144**](Body144.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form to update |  -  |
**422** | Can not update due to errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post(procore_company_id, project_id, bid_package_id, body143)

Create a Bid Form

Create a Bid Form for a Bid Package. A bid form is needed to submit a bid, since the bid will be made against the bid form.

### Example


```python
import procore_sdk
from procore_sdk.models.body143 import Body143
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    body143 = procore_sdk.Body143() # Body143 | 

    try:
        # Create a Bid Form
        api_response = api_instance.rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post(procore_company_id, project_id, bid_package_id, body143)
        print("The response of ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidFormsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bid_forms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **body143** | [**Body143**](Body143.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have right permissions |  -  |
**422** | Can not create due to errors |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

