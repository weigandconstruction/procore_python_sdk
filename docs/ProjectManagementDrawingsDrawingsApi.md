# procore_sdk.ProjectManagementDrawingsDrawingsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_drawing_areas_drawing_area_id_drawings_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_drawing_areas_drawing_area_id_drawings_get) | **GET** /rest/v1.0/drawing_areas/{drawing_area_id}/drawings | List drawings
[**rest_v10_drawing_areas_drawing_area_id_drawings_id_patch**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_drawing_areas_drawing_area_id_drawings_id_patch) | **PATCH** /rest/v1.0/drawing_areas/{drawing_area_id}/drawings/{id} | Update Drawing
[**rest_v10_projects_project_id_drawing_revision_terms_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_revision_terms_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_revision_terms | List drawing revision terms
[**rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_revisions/{drawing_revision_id}/drawing_tiles | List drawing tiles
[**rest_v10_projects_project_id_drawing_revisions_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_revisions_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_revisions | List drawing revisions
[**rest_v10_projects_project_id_drawing_revisions_id_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_revisions_id_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_revisions/{id} | Show Drawing Revision
[**rest_v10_projects_project_id_drawing_revisions_id_patch**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_revisions_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/drawing_revisions/{id} | Update Drawing Revision
[**rest_v10_projects_project_id_drawing_sets_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_sets_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_sets | List drawing sets
[**rest_v10_projects_project_id_drawing_sets_id_delete**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_sets_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/drawing_sets/{id} | Delete drawing set
[**rest_v10_projects_project_id_drawing_sets_id_patch**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_sets_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/drawing_sets/{id} | Update drawing set
[**rest_v10_projects_project_id_drawing_sets_post**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_sets_post) | **POST** /rest/v1.0/projects/{project_id}/drawing_sets | Create drawing set
[**rest_v10_projects_project_id_drawing_uploads_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_uploads_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_uploads | List drawing uploads
[**rest_v10_projects_project_id_drawing_uploads_id_delete**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_uploads_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/drawing_uploads/{id} | Delete drawing upload
[**rest_v10_projects_project_id_drawing_uploads_post**](ProjectManagementDrawingsDrawingsApi.md#rest_v10_projects_project_id_drawing_uploads_post) | **POST** /rest/v1.0/projects/{project_id}/drawing_uploads | Create drawing upload
[**rest_v11_drawing_areas_drawing_area_id_drawings_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_drawing_areas_drawing_area_id_drawings_get) | **GET** /rest/v1.1/drawing_areas/{drawing_area_id}/drawings | List drawings
[**rest_v11_drawing_areas_drawing_area_id_drawings_id_patch**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_drawing_areas_drawing_area_id_drawings_id_patch) | **PATCH** /rest/v1.1/drawing_areas/{drawing_area_id}/drawings/{id} | Update Drawing
[**rest_v11_drawing_areas_drawing_area_id_drawings_post**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_drawing_areas_drawing_area_id_drawings_post) | **POST** /rest/v1.1/drawing_areas/{drawing_area_id}/drawings | Create Drawing
[**rest_v11_projects_project_id_drawing_revision_terms_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_projects_project_id_drawing_revision_terms_get) | **GET** /rest/v1.1/projects/{project_id}/drawing_revision_terms | List drawing revision terms
[**rest_v11_projects_project_id_drawing_uploads_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_projects_project_id_drawing_uploads_get) | **GET** /rest/v1.1/projects/{project_id}/drawing_uploads | List drawing uploads
[**rest_v11_projects_project_id_drawing_uploads_id_delete**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_projects_project_id_drawing_uploads_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/drawing_uploads/{id} | Delete drawing upload
[**rest_v11_projects_project_id_drawing_uploads_id_get**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_projects_project_id_drawing_uploads_id_get) | **GET** /rest/v1.1/projects/{project_id}/drawing_uploads/{id} | Show Drawing Upload
[**rest_v11_projects_project_id_drawing_uploads_post**](ProjectManagementDrawingsDrawingsApi.md#rest_v11_projects_project_id_drawing_uploads_post) | **POST** /rest/v1.1/projects/{project_id}/drawing_uploads | Create drawing upload


# **rest_v10_drawing_areas_drawing_area_id_drawings_get**
> List[RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner] rest_v10_drawing_areas_drawing_area_id_drawings_get(procore_company_id, drawing_area_id, project_id=project_id, page=page, per_page=per_page)

List drawings

Returns a list of all Drawings for a specified drawing area.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner import RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    drawing_area_id = 56 # int | ID of the drawing area
    project_id = 56 # int | Unique identifier for the project. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List drawings
        api_response = api_instance.rest_v10_drawing_areas_drawing_area_id_drawings_get(procore_company_id, drawing_area_id, project_id=project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_drawing_areas_drawing_area_id_drawings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_drawing_areas_drawing_area_id_drawings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **drawing_area_id** | **int**| ID of the drawing area | 
 **project_id** | **int**| Unique identifier for the project. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner]**](RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_drawing_areas_drawing_area_id_drawings_id_patch**
> RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response rest_v10_drawing_areas_drawing_area_id_drawings_id_patch(procore_company_id, drawing_area_id, id, body88)

Update Drawing

Update specified Drawing

### Example


```python
import procore_sdk
from procore_sdk.models.body88 import Body88
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_post201_response import RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    drawing_area_id = 56 # int | ID of the drawing area
    id = 56 # int | Drawing ID
    body88 = procore_sdk.Body88() # Body88 | 

    try:
        # Update Drawing
        api_response = api_instance.rest_v10_drawing_areas_drawing_area_id_drawings_id_patch(procore_company_id, drawing_area_id, id, body88)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_drawing_areas_drawing_area_id_drawings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_drawing_areas_drawing_area_id_drawings_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **drawing_area_id** | **int**| ID of the drawing area | 
 **id** | **int**| Drawing ID | 
 **body88** | [**Body88**](Body88.md)|  | 

### Return type

[**RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response**](RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_revision_terms_get**
> List[DrawingRevisionTermSet] rest_v10_projects_project_id_drawing_revision_terms_get(procore_company_id, project_id, drawing_revision_ids=drawing_revision_ids)

List drawing revision terms

Returns extracted text terms and locations for a collection of Drawing Revisions.  Drawing Revisions which do not have any recorded term data will be omitted from the response. An empty term collection for a drawing indicates that the drawing has been processed, but that no terms were found.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_revision_term_set import DrawingRevisionTermSet
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    drawing_revision_ids = [56] # List[int] | Drawing Revisions to fetch extracted terms for. Limited to 50 revisions per call; clients should paginate larger collections. (optional)

    try:
        # List drawing revision terms
        api_response = api_instance.rest_v10_projects_project_id_drawing_revision_terms_get(procore_company_id, project_id, drawing_revision_ids=drawing_revision_ids)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revision_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revision_terms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **drawing_revision_ids** | [**List[int]**](int.md)| Drawing Revisions to fetch extracted terms for. Limited to 50 revisions per call; clients should paginate larger collections. | [optional] 

### Return type

[**List[DrawingRevisionTermSet]**](DrawingRevisionTermSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest  This is most likely caused by supplying too many revision ids. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get**
> RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get(procore_company_id, project_id, drawing_revision_id)

List drawing tiles

Lists the Drawing Tiles in the specified Drawing Revision along with the maximum Zoom Level and Tile Size.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response import RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    drawing_revision_id = 56 # int | ID of the drawing revision

    try:
        # List drawing tiles
        api_response = api_instance.rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get(procore_company_id, project_id, drawing_revision_id)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **drawing_revision_id** | **int**| ID of the drawing revision | 

### Return type

[**RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response**](RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_revisions_get**
> List[DrawingRevision] rest_v10_projects_project_id_drawing_revisions_get(procore_company_id, project_id, page=page, per_page=per_page, drawing_area_id=drawing_area_id, drawing_id=drawing_id, drawing_discipline_id=drawing_discipline_id, drawing_set_id=drawing_set_id, id=id, filters_ids=filters_ids, is_reviewed=is_reviewed, query=query, with_obsolete=with_obsolete, view=view)

List drawing revisions

Returns a list of all Drawing Revisions in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_revision import DrawingRevision
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    drawing_area_id = 56 # int | Filter by Drawing Area (optional)
    drawing_id = 56 # int | Filter by Drawing (optional)
    drawing_discipline_id = 56 # int | Filter by Drawing Discipline (optional)
    drawing_set_id = 56 # int | Filter by Drawing Set. To retreive revisions from current set add `drawing_set_id=current_set` to query (optional)
    id = [56] # List[int] | Filter by Drawing Revision ID To request specific drawing revision ids add `id[]=42&id[]=43` to query (optional)
    filters_ids = [56] # List[int] | Filter by Drawing Revisions ID To request specific drawing revision ids add `filters[ids]=[1,2,3]` to filters (optional)
    is_reviewed = True # bool | Filter by `reviewed` status (optional)
    query = 'query_example' # str | Filter by custom query (optional)
    with_obsolete = True # bool | Include obsolete drawing revisions. Obsolete drawing revisions are filtered by default. (optional)
    view = 'view_example' # str | Defines the type of view returned. Must be one of 'only_pdf_urls', 'only_ids', 'web_index', 'extended_coordinates', 'extended_files', 'extended_dpi' or 'android'. (optional)

    try:
        # List drawing revisions
        api_response = api_instance.rest_v10_projects_project_id_drawing_revisions_get(procore_company_id, project_id, page=page, per_page=per_page, drawing_area_id=drawing_area_id, drawing_id=drawing_id, drawing_discipline_id=drawing_discipline_id, drawing_set_id=drawing_set_id, id=id, filters_ids=filters_ids, is_reviewed=is_reviewed, query=query, with_obsolete=with_obsolete, view=view)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **drawing_area_id** | **int**| Filter by Drawing Area | [optional] 
 **drawing_id** | **int**| Filter by Drawing | [optional] 
 **drawing_discipline_id** | **int**| Filter by Drawing Discipline | [optional] 
 **drawing_set_id** | **int**| Filter by Drawing Set. To retreive revisions from current set add &#x60;drawing_set_id&#x3D;current_set&#x60; to query | [optional] 
 **id** | [**List[int]**](int.md)| Filter by Drawing Revision ID To request specific drawing revision ids add &#x60;id[]&#x3D;42&amp;id[]&#x3D;43&#x60; to query | [optional] 
 **filters_ids** | [**List[int]**](int.md)| Filter by Drawing Revisions ID To request specific drawing revision ids add &#x60;filters[ids]&#x3D;[1,2,3]&#x60; to filters | [optional] 
 **is_reviewed** | **bool**| Filter by &#x60;reviewed&#x60; status | [optional] 
 **query** | **str**| Filter by custom query | [optional] 
 **with_obsolete** | **bool**| Include obsolete drawing revisions. Obsolete drawing revisions are filtered by default. | [optional] 
 **view** | **str**| Defines the type of view returned. Must be one of &#39;only_pdf_urls&#39;, &#39;only_ids&#39;, &#39;web_index&#39;, &#39;extended_coordinates&#39;, &#39;extended_files&#39;, &#39;extended_dpi&#39; or &#39;android&#39;. | [optional] 

### Return type

[**List[DrawingRevision]**](DrawingRevision.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_revisions_id_get**
> DrawingRevision rest_v10_projects_project_id_drawing_revisions_id_get(procore_company_id, project_id, id)

Show Drawing Revision

Returns a specific Drawing Revision from the specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_revision import DrawingRevision
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Drawing Revision

    try:
        # Show Drawing Revision
        api_response = api_instance.rest_v10_projects_project_id_drawing_revisions_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Drawing Revision | 

### Return type

[**DrawingRevision**](DrawingRevision.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_revisions_id_patch**
> DrawingRevision1 rest_v10_projects_project_id_drawing_revisions_id_patch(procore_company_id, project_id, id, body89)

Update Drawing Revision

Update specified Drawing Revision

### Example


```python
import procore_sdk
from procore_sdk.models.body89 import Body89
from procore_sdk.models.drawing_revision1 import DrawingRevision1
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Drawing Revision
    body89 = procore_sdk.Body89() # Body89 | 

    try:
        # Update Drawing Revision
        api_response = api_instance.rest_v10_projects_project_id_drawing_revisions_id_patch(procore_company_id, project_id, id, body89)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_revisions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Drawing Revision | 
 **body89** | [**Body89**](Body89.md)|  | 

### Return type

[**DrawingRevision1**](DrawingRevision1.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_sets_get**
> List[DrawingSet] rest_v10_projects_project_id_drawing_sets_get(procore_company_id, project_id, page=page, per_page=per_page, filters_exclude_empty_sets=filters_exclude_empty_sets, filters_only_attachable_sets=filters_only_attachable_sets)

List drawing sets

Lists the Drawing Sets in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_set import DrawingSet
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_exclude_empty_sets = True # bool | If true, returns drawing sets that contain at least one drawing. (optional)
    filters_only_attachable_sets = True # bool | If true, returns drawing sets that contain at least one published drawing. (optional)

    try:
        # List drawing sets
        api_response = api_instance.rest_v10_projects_project_id_drawing_sets_get(procore_company_id, project_id, page=page, per_page=per_page, filters_exclude_empty_sets=filters_exclude_empty_sets, filters_only_attachable_sets=filters_only_attachable_sets)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_exclude_empty_sets** | **bool**| If true, returns drawing sets that contain at least one drawing. | [optional] 
 **filters_only_attachable_sets** | **bool**| If true, returns drawing sets that contain at least one published drawing. | [optional] 

### Return type

[**List[DrawingSet]**](DrawingSet.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_sets_id_delete**
> rest_v10_projects_project_id_drawing_sets_id_delete(procore_company_id, project_id, id)

Delete drawing set

Delete a specified Drawing Set.

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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the drawing set

    try:
        # Delete drawing set
        api_instance.rest_v10_projects_project_id_drawing_sets_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the drawing set | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_sets_id_patch**
> DrawingSet rest_v10_projects_project_id_drawing_sets_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_drawing_sets_id_patch_request)

Update drawing set

Update an existing Drawing Set in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_set import DrawingSet
from procore_sdk.models.rest_v10_projects_project_id_drawing_sets_id_patch_request import RestV10ProjectsProjectIdDrawingSetsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the drawing set
    rest_v10_projects_project_id_drawing_sets_id_patch_request = procore_sdk.RestV10ProjectsProjectIdDrawingSetsIdPatchRequest() # RestV10ProjectsProjectIdDrawingSetsIdPatchRequest | 

    try:
        # Update drawing set
        api_response = api_instance.rest_v10_projects_project_id_drawing_sets_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_drawing_sets_id_patch_request)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the drawing set | 
 **rest_v10_projects_project_id_drawing_sets_id_patch_request** | [**RestV10ProjectsProjectIdDrawingSetsIdPatchRequest**](RestV10ProjectsProjectIdDrawingSetsIdPatchRequest.md)|  | 

### Return type

[**DrawingSet**](DrawingSet.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_sets_post**
> DrawingSet rest_v10_projects_project_id_drawing_sets_post(procore_company_id, project_id, rest_v10_projects_project_id_drawing_sets_post_request)

Create drawing set

Create a new Drawing Set in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_set import DrawingSet
from procore_sdk.models.rest_v10_projects_project_id_drawing_sets_post_request import RestV10ProjectsProjectIdDrawingSetsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_drawing_sets_post_request = procore_sdk.RestV10ProjectsProjectIdDrawingSetsPostRequest() # RestV10ProjectsProjectIdDrawingSetsPostRequest | 

    try:
        # Create drawing set
        api_response = api_instance.rest_v10_projects_project_id_drawing_sets_post(procore_company_id, project_id, rest_v10_projects_project_id_drawing_sets_post_request)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_drawing_sets_post_request** | [**RestV10ProjectsProjectIdDrawingSetsPostRequest**](RestV10ProjectsProjectIdDrawingSetsPostRequest.md)|  | 

### Return type

[**DrawingSet**](DrawingSet.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_uploads_get**
> List[DrawingUpload1] rest_v10_projects_project_id_drawing_uploads_get(procore_company_id, project_id, page=page, per_page=per_page)

List drawing uploads

Returns a list of all Drawing Uploads in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_upload1 import DrawingUpload1
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List drawing uploads
        api_response = api_instance.rest_v10_projects_project_id_drawing_uploads_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_uploads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_uploads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[DrawingUpload1]**](DrawingUpload1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_uploads_id_delete**
> rest_v10_projects_project_id_drawing_uploads_id_delete(procore_company_id, project_id, id)

Delete drawing upload

Delete an unreviewed Drawing Upload.

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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the drawing upload

    try:
        # Delete drawing upload
        api_instance.rest_v10_projects_project_id_drawing_uploads_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_uploads_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the drawing upload | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_uploads_post**
> DrawingUpload1 rest_v10_projects_project_id_drawing_uploads_post(procore_company_id, project_id, drawing_set_id, idempotency_token=idempotency_token, files=files, upload_uuids=upload_uuids, drawing_area_id=drawing_area_id, drawing_number_contains_revision=drawing_number_contains_revision, drawing_date=drawing_date, received_date=received_date, get_info_from_filename=get_info_from_filename)

Create drawing upload

Create a new Drawing Upload in the specified project.  It creates one `DrawingUpload`, which includes a `DrawingLogImport` and a `ProstoreFile` for each file uploaded. Sidekiq then sends them to the image processing server.  First, it will try to process `files` parameter, if is empty, it will use `upload_uuids`.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_upload1 import DrawingUpload1
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    drawing_set_id = 56 # int | Drawing Set ID
    idempotency_token = 'idempotency_token_example' # str | Unique idempotent token (optional)
    files = ['files_example'] # List[str] | One or more files in PDF format to include in the upload. *To upload drawings you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `files[]` as files. *Required only if upload_uuids is empty (optional)
    upload_uuids = ['upload_uuids_example'] # List[str] | Array of uploaded files UUIDs. *Required only if files is empty (optional)
    drawing_area_id = 56 # int | Drawing Area ID *Required only if Drawing Area is turned on (optional)
    drawing_number_contains_revision = True # bool | Drawing number contains revision status (optional)
    drawing_date = '2013-10-20' # date | Drawing date (optional)
    received_date = '2013-10-20' # date | Received date (optional)
    get_info_from_filename = True # bool | Get info from filename (optional)

    try:
        # Create drawing upload
        api_response = api_instance.rest_v10_projects_project_id_drawing_uploads_post(procore_company_id, project_id, drawing_set_id, idempotency_token=idempotency_token, files=files, upload_uuids=upload_uuids, drawing_area_id=drawing_area_id, drawing_number_contains_revision=drawing_number_contains_revision, drawing_date=drawing_date, received_date=received_date, get_info_from_filename=get_info_from_filename)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v10_projects_project_id_drawing_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **drawing_set_id** | **int**| Drawing Set ID | 
 **idempotency_token** | **str**| Unique idempotent token | [optional] 
 **files** | [**List[str]**](str.md)| One or more files in PDF format to include in the upload. *To upload drawings you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;files[]&#x60; as files. *Required only if upload_uuids is empty | [optional] 
 **upload_uuids** | [**List[str]**](str.md)| Array of uploaded files UUIDs. *Required only if files is empty | [optional] 
 **drawing_area_id** | **int**| Drawing Area ID *Required only if Drawing Area is turned on | [optional] 
 **drawing_number_contains_revision** | **bool**| Drawing number contains revision status | [optional] 
 **drawing_date** | **date**| Drawing date | [optional] 
 **received_date** | **date**| Received date | [optional] 
 **get_info_from_filename** | **bool**| Get info from filename | [optional] 

### Return type

[**DrawingUpload1**](DrawingUpload1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Duplicate Idempotency-token header) |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_drawing_areas_drawing_area_id_drawings_get**
> List[RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner] rest_v11_drawing_areas_drawing_area_id_drawings_get(procore_company_id, drawing_area_id, project_id=project_id, page=page, per_page=per_page)

List drawings

Returns a list of all Drawings for a specified drawing area.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner import RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    drawing_area_id = 56 # int | ID of the drawing area
    project_id = 56 # int | Unique identifier for the project. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List drawings
        api_response = api_instance.rest_v11_drawing_areas_drawing_area_id_drawings_get(procore_company_id, drawing_area_id, project_id=project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **drawing_area_id** | **int**| ID of the drawing area | 
 **project_id** | **int**| Unique identifier for the project. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner]**](RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_drawing_areas_drawing_area_id_drawings_id_patch**
> RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response rest_v11_drawing_areas_drawing_area_id_drawings_id_patch(procore_company_id, drawing_area_id, id, body88)

Update Drawing

Update specified Drawing

### Example


```python
import procore_sdk
from procore_sdk.models.body88 import Body88
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_post201_response import RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    drawing_area_id = 56 # int | ID of the drawing area
    id = 56 # int | Drawing ID
    body88 = procore_sdk.Body88() # Body88 | 

    try:
        # Update Drawing
        api_response = api_instance.rest_v11_drawing_areas_drawing_area_id_drawings_id_patch(procore_company_id, drawing_area_id, id, body88)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **drawing_area_id** | **int**| ID of the drawing area | 
 **id** | **int**| Drawing ID | 
 **body88** | [**Body88**](Body88.md)|  | 

### Return type

[**RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response**](RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_drawing_areas_drawing_area_id_drawings_post**
> RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response rest_v11_drawing_areas_drawing_area_id_drawings_post(procore_company_id, drawing_area_id, body87)

Create Drawing

Create specified Drawing. For additional information on using the Create Drawing Upload endpoint, see the [Direct Drawing Uploads](https://developers.procore.com/documentation/tutorial-direct-drawing-uploads) tutorial.

### Example


```python
import procore_sdk
from procore_sdk.models.body87 import Body87
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_post201_response import RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    drawing_area_id = 56 # int | ID of the drawing area
    body87 = procore_sdk.Body87() # Body87 | 

    try:
        # Create Drawing
        api_response = api_instance.rest_v11_drawing_areas_drawing_area_id_drawings_post(procore_company_id, drawing_area_id, body87)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_drawing_areas_drawing_area_id_drawings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **drawing_area_id** | **int**| ID of the drawing area | 
 **body87** | [**Body87**](Body87.md)|  | 

### Return type

[**RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response**](RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_drawing_revision_terms_get**
> List[DrawingRevisionTermSet] rest_v11_projects_project_id_drawing_revision_terms_get(procore_company_id, project_id, drawing_revision_ids=drawing_revision_ids)

List drawing revision terms

Returns extracted text terms and locations for a collection of Drawing Revisions.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_revision_term_set import DrawingRevisionTermSet
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    drawing_revision_ids = [56] # List[int] | Drawing Revisions to fetch extracted terms for. Limited to 50 revisions per call; clients should paginate larger collections. (optional)

    try:
        # List drawing revision terms
        api_response = api_instance.rest_v11_projects_project_id_drawing_revision_terms_get(procore_company_id, project_id, drawing_revision_ids=drawing_revision_ids)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_revision_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_revision_terms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **drawing_revision_ids** | [**List[int]**](int.md)| Drawing Revisions to fetch extracted terms for. Limited to 50 revisions per call; clients should paginate larger collections. | [optional] 

### Return type

[**List[DrawingRevisionTermSet]**](DrawingRevisionTermSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BadRequest  This is most likely caused by supplying too many revision ids. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_drawing_uploads_get**
> List[DrawingUpload] rest_v11_projects_project_id_drawing_uploads_get(procore_company_id, project_id, page=page, per_page=per_page, view=view)

List drawing uploads

Returns a list of all Drawing Uploads in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_upload import DrawingUpload
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | Specifies the level of detail returned in the response. The 'with_drawing_log_imports' view provides additional data as shown below. The 'normal' view is the default if not specified. (optional)

    try:
        # List drawing uploads
        api_response = api_instance.rest_v11_projects_project_id_drawing_uploads_get(procore_company_id, project_id, page=page, per_page=per_page, view=view)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| Specifies the level of detail returned in the response. The &#39;with_drawing_log_imports&#39; view provides additional data as shown below. The &#39;normal&#39; view is the default if not specified. | [optional] 

### Return type

[**List[DrawingUpload]**](DrawingUpload.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_drawing_uploads_id_delete**
> rest_v11_projects_project_id_drawing_uploads_id_delete(procore_company_id, id, project_id, view=view)

Delete drawing upload

Delete an unreviewed Drawing Upload.

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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Drawing Upload ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies the level of detail returned in the response. The 'with_drawing_log_imports' view provides additional data as shown below. The 'normal' view is the default if not specified. (optional)

    try:
        # Delete drawing upload
        api_instance.rest_v11_projects_project_id_drawing_uploads_id_delete(procore_company_id, id, project_id, view=view)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Drawing Upload ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies the level of detail returned in the response. The &#39;with_drawing_log_imports&#39; view provides additional data as shown below. The &#39;normal&#39; view is the default if not specified. | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_drawing_uploads_id_get**
> DrawingUpload rest_v11_projects_project_id_drawing_uploads_id_get(procore_company_id, id, project_id, view=view)

Show Drawing Upload

Get the details of a single Drawing Upload

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_upload import DrawingUpload
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Drawing Upload ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies the level of detail returned in the response. The 'with_drawing_log_imports' view provides additional data as shown below. The 'normal' view is the default if not specified. (optional)

    try:
        # Show Drawing Upload
        api_response = api_instance.rest_v11_projects_project_id_drawing_uploads_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Drawing Upload ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies the level of detail returned in the response. The &#39;with_drawing_log_imports&#39; view provides additional data as shown below. The &#39;normal&#39; view is the default if not specified. | [optional] 

### Return type

[**DrawingUpload**](DrawingUpload.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_drawing_uploads_post**
> DrawingUpload1 rest_v11_projects_project_id_drawing_uploads_post(procore_company_id, project_id, idempotency_token=idempotency_token, drawing_upload=drawing_upload)

Create drawing upload

Create a new Drawing Upload in the specified project.  It creates one `DrawingUpload`, which includes a `DrawingLogImport` and a `ProstoreFile` for each file uploaded. The Drawing Upload will be processed asynchronously after the response. For additional information on using the Create Drawing endpoint, see [Direct Drawing Uploads](/documentation/tutorial-direct-drawing-uploads) tutorial.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_upload import DrawingUpload
from procore_sdk.models.drawing_upload1 import DrawingUpload1
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    idempotency_token = 'idempotency_token_example' # str | Unique idempotent token (optional)
    drawing_upload = procore_sdk.DrawingUpload() # DrawingUpload |  (optional)

    try:
        # Create drawing upload
        api_response = api_instance.rest_v11_projects_project_id_drawing_uploads_post(procore_company_id, project_id, idempotency_token=idempotency_token, drawing_upload=drawing_upload)
        print("The response of ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingsApi->rest_v11_projects_project_id_drawing_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **idempotency_token** | **str**| Unique idempotent token | [optional] 
 **drawing_upload** | [**DrawingUpload**](DrawingUpload.md)|  | [optional] 

### Return type

[**DrawingUpload1**](DrawingUpload1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Duplicate Idempotency-token header) |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

