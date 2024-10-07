# procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_work_classifications_bulk_update_patch**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_classifications/bulk_update | Update all classification
[**rest_v10_projects_project_id_work_classifications_get**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_get) | **GET** /rest/v1.0/projects/{project_id}/work_classifications | List all classifications
[**rest_v10_projects_project_id_work_classifications_id_delete**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/work_classifications/{id} | Delete a classification
[**rest_v10_projects_project_id_work_classifications_id_get**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_id_get) | **GET** /rest/v1.0/projects/{project_id}/work_classifications/{id} | Show classification
[**rest_v10_projects_project_id_work_classifications_id_patch**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_classifications/{id} | Update a classification
[**rest_v10_projects_project_id_work_classifications_initial_setup_post**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_initial_setup_post) | **POST** /rest/v1.0/projects/{project_id}/work_classifications/initial_setup | Create Company Classifications For Project
[**rest_v10_projects_project_id_work_classifications_post**](FieldProductivityWorkClassificationWorkClassificationProjectLevelApi.md#rest_v10_projects_project_id_work_classifications_post) | **POST** /rest/v1.0/projects/{project_id}/work_classifications | Create a new classification


# **rest_v10_projects_project_id_work_classifications_bulk_update_patch**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_projects_project_id_work_classifications_bulk_update_patch(procore_company_id, project_id, work_classification_bulk_body)

Update all classification

Activating/deactivating all classifications associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
from procore_sdk.models.work_classification_bulk_body import WorkClassificationBulkBody
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    work_classification_bulk_body = procore_sdk.WorkClassificationBulkBody() # WorkClassificationBulkBody | 

    try:
        # Update all classification
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_bulk_update_patch(procore_company_id, project_id, work_classification_bulk_body)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **work_classification_bulk_body** | [**WorkClassificationBulkBody**](WorkClassificationBulkBody.md)|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Invalid entry parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_classifications_get**
> List[RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner] rest_v10_projects_project_id_work_classifications_get(procore_company_id, project_id, page=page, per_page=per_page)

List all classifications

Return a list of all classifications with details for a specified project.

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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all classifications
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_projects_project_id_work_classifications_id_delete**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_projects_project_id_work_classifications_id_delete(procore_company_id, project_id, id)

Delete a classification

Deleting a classification associated with the specified project.

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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the classification

    try:
        # Delete a classification
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the classification | 

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
**200** | Classification deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_classifications_id_get**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_projects_project_id_work_classifications_id_get(procore_company_id, project_id, id)

Show classification

Return classification detailed information.

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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show classification
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_projects_project_id_work_classifications_id_patch**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_projects_project_id_work_classifications_id_patch(procore_company_id, project_id, id, work_classification_body)

Update a classification

Updating a classification associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
from procore_sdk.models.work_classification_body import WorkClassificationBody
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the classification
    work_classification_body = procore_sdk.WorkClassificationBody() # WorkClassificationBody | 

    try:
        # Update a classification
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_id_patch(procore_company_id, project_id, id, work_classification_body)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the classification | 
 **work_classification_body** | [**WorkClassificationBody**](WorkClassificationBody.md)|  | 

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a classification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_classifications_initial_setup_post**
> List[RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner] rest_v10_projects_project_id_work_classifications_initial_setup_post(procore_company_id, project_id)

Create Company Classifications For Project

All company work classifications are created for the project

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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Create Company Classifications For Project
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_initial_setup_post(procore_company_id, project_id)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_initial_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_initial_setup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**201** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | Forbidden |  -  |
**422** | Error creating a Classification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_classifications_post**
> RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner rest_v10_projects_project_id_work_classifications_post(procore_company_id, project_id, work_classification_body)

Create a new classification

Create a new classification associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner
from procore_sdk.models.work_classification_body import WorkClassificationBody
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
    api_instance = procore_sdk.FieldProductivityWorkClassificationWorkClassificationProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    work_classification_body = procore_sdk.WorkClassificationBody() # WorkClassificationBody | 

    try:
        # Create a new classification
        api_response = api_instance.rest_v10_projects_project_id_work_classifications_post(procore_company_id, project_id, work_classification_body)
        print("The response of FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityWorkClassificationWorkClassificationProjectLevelApi->rest_v10_projects_project_id_work_classifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **work_classification_body** | [**WorkClassificationBody**](WorkClassificationBody.md)|  | 

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
**403** | Forbidden |  -  |
**422** | Error creating a Classification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

