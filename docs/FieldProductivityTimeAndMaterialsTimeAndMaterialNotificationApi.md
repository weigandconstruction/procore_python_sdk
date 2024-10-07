# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_notifications_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi.md#rest_v10_projects_project_id_time_and_material_notifications_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_notifications | Delete a Time And Material Notification
[**rest_v10_projects_project_id_time_and_material_notifications_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi.md#rest_v10_projects_project_id_time_and_material_notifications_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_notifications | Show Time And Material Notification
[**rest_v10_projects_project_id_time_and_material_notifications_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi.md#rest_v10_projects_project_id_time_and_material_notifications_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_notifications | Update a Time And Material Notification
[**rest_v10_projects_project_id_time_and_material_notifications_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi.md#rest_v10_projects_project_id_time_and_material_notifications_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_notifications | Create a new Time And Material Notification


# **rest_v10_projects_project_id_time_and_material_notifications_delete**
> RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response rest_v10_projects_project_id_time_and_material_notifications_delete(procore_company_id, project_id)

Delete a Time And Material Notification

Deleting a Time And Material Notification associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_notifications_get200_response import RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete a Time And Material Notification
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_notifications_delete(procore_company_id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response**](RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Notification deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_notifications_get**
> RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response rest_v10_projects_project_id_time_and_material_notifications_get(procore_company_id, project_id)

Show Time And Material Notification

Return Time And Material Notification detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_notifications_get200_response import RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Time And Material Notification
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_notifications_get(procore_company_id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response**](RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.md)

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

# **rest_v10_projects_project_id_time_and_material_notifications_patch**
> RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response rest_v10_projects_project_id_time_and_material_notifications_patch(procore_company_id, project_id, time_and_material_notification_body, run_configurable_validations=run_configurable_validations)

Update a Time And Material Notification

Updating a Time And Material Notification associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_notifications_get200_response import RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response
from procore_sdk.models.time_and_material_notification_body import TimeAndMaterialNotificationBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_notification_body = procore_sdk.TimeAndMaterialNotificationBody() # TimeAndMaterialNotificationBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update a Time And Material Notification
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_notifications_patch(procore_company_id, project_id, time_and_material_notification_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_notification_body** | [**TimeAndMaterialNotificationBody**](TimeAndMaterialNotificationBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response**](RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Notification updated |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a Time And Material Notification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_notifications_post**
> RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response rest_v10_projects_project_id_time_and_material_notifications_post(procore_company_id, project_id, time_and_material_notification_body, run_configurable_validations=run_configurable_validations)

Create a new Time And Material Notification

Create a new Time And Material Notification associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_notifications_get200_response import RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response
from procore_sdk.models.time_and_material_notification_body import TimeAndMaterialNotificationBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_notification_body = procore_sdk.TimeAndMaterialNotificationBody() # TimeAndMaterialNotificationBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create a new Time And Material Notification
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_notifications_post(procore_company_id, project_id, time_and_material_notification_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialNotificationApi->rest_v10_projects_project_id_time_and_material_notifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_notification_body** | [**TimeAndMaterialNotificationBody**](TimeAndMaterialNotificationBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response**](RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Time And Material Notification Created Succesfully |  -  |
**403** | Forbidden |  -  |
**422** | Error Creating a Time And Material Notification |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

