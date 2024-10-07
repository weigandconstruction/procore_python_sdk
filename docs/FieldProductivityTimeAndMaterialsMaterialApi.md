# procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_materials_bulk_create_post**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/materials/bulk_create | Bulk Create Materials
[**rest_v10_projects_project_id_materials_bulk_destroy_delete**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/materials/bulk_destroy | Bulk Delete Materials
[**rest_v10_projects_project_id_materials_bulk_update_patch**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/materials/bulk_update | Bulk Update Materials
[**rest_v10_projects_project_id_materials_get**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_get) | **GET** /rest/v1.0/projects/{project_id}/materials | List Materials
[**rest_v10_projects_project_id_materials_id_delete**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/materials/{id} | Delete Material
[**rest_v10_projects_project_id_materials_id_get**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_id_get) | **GET** /rest/v1.0/projects/{project_id}/materials/{id} | Show Material
[**rest_v10_projects_project_id_materials_id_patch**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/materials/{id} | Update Material
[**rest_v10_projects_project_id_materials_post**](FieldProductivityTimeAndMaterialsMaterialApi.md#rest_v10_projects_project_id_materials_post) | **POST** /rest/v1.0/projects/{project_id}/materials | Create Material


# **rest_v10_projects_project_id_materials_bulk_create_post**
> List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner] rest_v10_projects_project_id_materials_bulk_create_post(procore_company_id, project_id, material_bulk_create_body)

Bulk Create Materials

Bulk create Material entries with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.material_bulk_create_body import MaterialBulkCreateBody
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    material_bulk_create_body = procore_sdk.MaterialBulkCreateBody() # MaterialBulkCreateBody | 

    try:
        # Bulk Create Materials
        api_response = api_instance.rest_v10_projects_project_id_materials_bulk_create_post(procore_company_id, project_id, material_bulk_create_body)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **material_bulk_create_body** | [**MaterialBulkCreateBody**](MaterialBulkCreateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner]**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner] rest_v10_projects_project_id_materials_bulk_destroy_delete(procore_company_id, project_id, material_bulk_destroy_body)

Bulk Delete Materials

Bulk delete Material entries with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.material_bulk_destroy_body import MaterialBulkDestroyBody
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    material_bulk_destroy_body = procore_sdk.MaterialBulkDestroyBody() # MaterialBulkDestroyBody | 

    try:
        # Bulk Delete Materials
        api_response = api_instance.rest_v10_projects_project_id_materials_bulk_destroy_delete(procore_company_id, project_id, material_bulk_destroy_body)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **material_bulk_destroy_body** | [**MaterialBulkDestroyBody**](MaterialBulkDestroyBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner]**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_bulk_update_patch**
> List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner] rest_v10_projects_project_id_materials_bulk_update_patch(procore_company_id, project_id, material_bulk_update_body)

Bulk Update Materials

Bulk update Material entries with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.material_bulk_update_body import MaterialBulkUpdateBody
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    material_bulk_update_body = procore_sdk.MaterialBulkUpdateBody() # MaterialBulkUpdateBody | 

    try:
        # Bulk Update Materials
        api_response = api_instance.rest_v10_projects_project_id_materials_bulk_update_patch(procore_company_id, project_id, material_bulk_update_body)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **material_bulk_update_body** | [**MaterialBulkUpdateBody**](MaterialBulkUpdateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner]**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_get**
> List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner] rest_v10_projects_project_id_materials_get(procore_company_id, project_id, page=page, per_page=per_page)

List Materials

Return a list of all Materials

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Materials
        api_response = api_instance.rest_v10_projects_project_id_materials_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdMaterialsGet200ResponseInner]**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_materials_id_delete**
> RestV10ProjectsProjectIdMaterialsGet200ResponseInner rest_v10_projects_project_id_materials_id_delete(procore_company_id, id, project_id)

Delete Material

Detete a specific Material.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Material
        api_response = api_instance.rest_v10_projects_project_id_materials_id_delete(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdMaterialsGet200ResponseInner**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_id_get**
> RestV10ProjectsProjectIdMaterialsGet200ResponseInner rest_v10_projects_project_id_materials_id_get(procore_company_id, id, project_id)

Show Material

Return detailed information about a specific Material.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Material
        api_response = api_instance.rest_v10_projects_project_id_materials_id_get(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdMaterialsGet200ResponseInner**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_id_patch**
> RestV10ProjectsProjectIdMaterialsGet200ResponseInner rest_v10_projects_project_id_materials_id_patch(procore_company_id, id, project_id, material_body)

Update Material

Update a specified Material.

### Example


```python
import procore_sdk
from procore_sdk.models.material_body import MaterialBody
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project
    project_id = 56 # int | Unique identifier for the project.
    material_body = procore_sdk.MaterialBody() # MaterialBody | 

    try:
        # Update Material
        api_response = api_instance.rest_v10_projects_project_id_materials_id_patch(procore_company_id, id, project_id, material_body)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project | 
 **project_id** | **int**| Unique identifier for the project. | 
 **material_body** | [**MaterialBody**](MaterialBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdMaterialsGet200ResponseInner**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_materials_post**
> RestV10ProjectsProjectIdMaterialsGet200ResponseInner rest_v10_projects_project_id_materials_post(procore_company_id, project_id, material_body)

Create Material

Create a new Material Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.material_body import MaterialBody
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsMaterialApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    material_body = procore_sdk.MaterialBody() # MaterialBody | 

    try:
        # Create Material
        api_response = api_instance.rest_v10_projects_project_id_materials_post(procore_company_id, project_id, material_body)
        print("The response of FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsMaterialApi->rest_v10_projects_project_id_materials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **material_body** | [**MaterialBody**](MaterialBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdMaterialsGet200ResponseInner**](RestV10ProjectsProjectIdMaterialsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

