# procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_categories_get**](FieldProductivityManagedEquipmentEquipmentCategoryApi.md#rest_v10_companies_company_id_managed_equipment_categories_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_categories | List all equipment categories
[**rest_v10_companies_company_id_managed_equipment_categories_id_delete**](FieldProductivityManagedEquipmentEquipmentCategoryApi.md#rest_v10_companies_company_id_managed_equipment_categories_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_categories/{id} | Delete Equipment Category
[**rest_v10_companies_company_id_managed_equipment_categories_id_get**](FieldProductivityManagedEquipmentEquipmentCategoryApi.md#rest_v10_companies_company_id_managed_equipment_categories_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_categories/{id} | Show an equipment category
[**rest_v10_companies_company_id_managed_equipment_categories_id_patch**](FieldProductivityManagedEquipmentEquipmentCategoryApi.md#rest_v10_companies_company_id_managed_equipment_categories_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_categories/{id} | Update Equipment Category
[**rest_v10_companies_company_id_managed_equipment_categories_post**](FieldProductivityManagedEquipmentEquipmentCategoryApi.md#rest_v10_companies_company_id_managed_equipment_categories_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_categories | Create equipment Category


# **rest_v10_companies_company_id_managed_equipment_categories_get**
> List[ManagedEquipmentCategory] rest_v10_companies_company_id_managed_equipment_categories_get(procore_company_id, company_id, page=page, per_page=per_page)

List all equipment categories

Return a list of all equipment Categories.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all equipment categories
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_categories_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ManagedEquipmentCategory]**](ManagedEquipmentCategory.md)

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

# **rest_v10_companies_company_id_managed_equipment_categories_id_delete**
> ManagedEquipmentCategory rest_v10_companies_company_id_managed_equipment_categories_id_delete(procore_company_id, company_id, id)

Delete Equipment Category

Detete a specific Equipment Category.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Equipment Category

    try:
        # Delete Equipment Category
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_categories_id_delete(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Equipment Category | 

### Return type

[**ManagedEquipmentCategory**](ManagedEquipmentCategory.md)

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

# **rest_v10_companies_company_id_managed_equipment_categories_id_get**
> ManagedEquipmentCategory rest_v10_companies_company_id_managed_equipment_categories_id_get(procore_company_id, company_id, id)

Show an equipment category

Return detailed information about a specific equipment Category.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the equipment category

    try:
        # Show an equipment category
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_categories_id_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the equipment category | 

### Return type

[**ManagedEquipmentCategory**](ManagedEquipmentCategory.md)

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

# **rest_v10_companies_company_id_managed_equipment_categories_id_patch**
> ManagedEquipmentCategory rest_v10_companies_company_id_managed_equipment_categories_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_categories_post_request=rest_v10_companies_company_id_managed_equipment_categories_post_request)

Update Equipment Category

Update a specified equipment category.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_categories_post_request import RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Equipment Category
    rest_v10_companies_company_id_managed_equipment_categories_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest |  (optional)

    try:
        # Update Equipment Category
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_categories_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_categories_post_request=rest_v10_companies_company_id_managed_equipment_categories_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Equipment Category | 
 **rest_v10_companies_company_id_managed_equipment_categories_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentCategory**](ManagedEquipmentCategory.md)

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

# **rest_v10_companies_company_id_managed_equipment_categories_post**
> ManagedEquipmentCategory rest_v10_companies_company_id_managed_equipment_categories_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_categories_post_request=rest_v10_companies_company_id_managed_equipment_categories_post_request)

Create equipment Category

Create a new equipment Category Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_categories_post_request import RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentCategoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_categories_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest |  (optional)

    try:
        # Create equipment Category
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_categories_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_categories_post_request=rest_v10_companies_company_id_managed_equipment_categories_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentCategoryApi->rest_v10_companies_company_id_managed_equipment_categories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_categories_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentCategoriesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentCategory**](ManagedEquipmentCategory.md)

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

