# procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_work_classifications_get**](FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi.md#rest_v10_companies_company_id_work_classifications_get) | **GET** /rest/v1.0/companies/{company_id}/work_classifications | List all Classification
[**rest_v10_companies_company_id_work_classifications_id_delete**](FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi.md#rest_v10_companies_company_id_work_classifications_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/work_classifications/{id} | Delete Classification
[**rest_v10_companies_company_id_work_classifications_id_get**](FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi.md#rest_v10_companies_company_id_work_classifications_id_get) | **GET** /rest/v1.0/companies/{company_id}/work_classifications/{id} | Show Classification
[**rest_v10_companies_company_id_work_classifications_id_patch**](FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi.md#rest_v10_companies_company_id_work_classifications_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/work_classifications/{id} | Update Classification
[**rest_v10_companies_company_id_work_classifications_post**](FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi.md#rest_v10_companies_company_id_work_classifications_post) | **POST** /rest/v1.0/companies/{company_id}/work_classifications | Create Classification


# **rest_v10_companies_company_id_work_classifications_get**
> List[RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner] rest_v10_companies_company_id_work_classifications_get(procore_company_id, company_id, page=page, per_page=per_page)

List all Classification

Return a list of all Classification with details for a specified company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all Classification
        api_response = api_instance.rest_v10_companies_company_id_work_classifications_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner]**](RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_classifications_id_delete**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_companies_company_id_work_classifications_id_delete(procore_company_id, company_id, id)

Delete Classification

Deleting a Classification

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Classification

    try:
        # Delete Classification
        api_response = api_instance.rest_v10_companies_company_id_work_classifications_id_delete(procore_company_id, company_id, id)
        print("The response of FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Classification | 

### Return type

[**RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner**](RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_classifications_id_get**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_companies_company_id_work_classifications_id_get(procore_company_id, company_id, id)

Show Classification

Return Classification detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # Show Classification
        api_response = api_instance.rest_v10_companies_company_id_work_classifications_id_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner**](RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_classifications_id_patch**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_companies_company_id_work_classifications_id_patch(procore_company_id, company_id, id, work_classification_body1)

Update Classification

Updating a Classification

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
from procore_sdk.models.work_classification_body1 import WorkClassificationBody1
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Classification
    work_classification_body1 = procore_sdk.WorkClassificationBody1() # WorkClassificationBody1 | 

    try:
        # Update Classification
        api_response = api_instance.rest_v10_companies_company_id_work_classifications_id_patch(procore_company_id, company_id, id, work_classification_body1)
        print("The response of FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Classification | 
 **work_classification_body1** | [**WorkClassificationBody1**](WorkClassificationBody1.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner**](RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Classification updated |  -  |
**422** | Error updating a Classification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_classifications_post**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_companies_company_id_work_classifications_post(procore_company_id, company_id, work_classification_body1)

Create Classification

Create a new Classification associated with the specified company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
from procore_sdk.models.work_classification_body1 import WorkClassificationBody1
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    work_classification_body1 = procore_sdk.WorkClassificationBody1() # WorkClassificationBody1 | 

    try:
        # Create Classification
        api_response = api_instance.rest_v10_companies_company_id_work_classifications_post(procore_company_id, company_id, work_classification_body1)
        print("The response of FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationCompanyLevelApi->rest_v10_companies_company_id_work_classifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **work_classification_body1** | [**WorkClassificationBody1**](WorkClassificationBody1.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner**](RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Classification Created Succesfully |  -  |
**422** | Error creating a Classification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

