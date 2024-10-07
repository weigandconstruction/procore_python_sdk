# procore_sdk.CoreCompanyDirectoryCompanyVendorsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_vendors_get**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_get) | **GET** /rest/v1.0/vendors | List company vendors
[**rest_v10_vendors_id_business_register_patch**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_id_business_register_patch) | **PATCH** /rest/v1.0/vendors/{id}/business_register | Update Company Vendor Business Register
[**rest_v10_vendors_id_business_register_post**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_id_business_register_post) | **POST** /rest/v1.0/vendors/{id}/business_register | Create Company Vendor Business Register
[**rest_v10_vendors_id_get**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_id_get) | **GET** /rest/v1.0/vendors/{id} | Show company vendor
[**rest_v10_vendors_id_patch**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_id_patch) | **PATCH** /rest/v1.0/vendors/{id} | Update company vendor
[**rest_v10_vendors_post**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_post) | **POST** /rest/v1.0/vendors | Create company vendor
[**rest_v10_vendors_sync_patch**](CoreCompanyDirectoryCompanyVendorsApi.md#rest_v10_vendors_sync_patch) | **PATCH** /rest/v1.0/vendors/sync | Sync company vendors


# **rest_v10_vendors_get**
> List[RestV10VendorsGet200ResponseInner] rest_v10_vendors_get(procore_company_id, company_id, view=view, page=page, per_page=per_page, filters_origin_id=filters_origin_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, sort=sort)

List company vendors

Return a list of all Vendors associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_vendors_get200_response_inner import RestV10VendorsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_search = 'filters_search_example' # str | Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number (optional)
    filters_created_at = '2013-10-20T19:20:30+01:00' # datetime | Return items within a specific created at ISO8601 datetime range (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Return items within a specific updated at ISO8601 datetime range (optional)
    filters_standard_cost_code_id = [56] # List[int] | Returns vendors associated with the specified standard cost code id(s) (optional)
    filters_trade_id = [56] # List[int] | Returns vendors associated with the specified trade id(s) (optional)
    filters_id = [56] # List[int] | Returns vendors with the specified id(s) (optional)
    filters_parent_id = [56] # List[int] | Returns vendors with the specified parent id(s) (optional)
    sort = 'sort_example' # str | Return items with the specified sort (optional)

    try:
        # List company vendors
        api_response = api_instance.rest_v10_vendors_get(procore_company_id, company_id, view=view, page=page, per_page=per_page, filters_origin_id=filters_origin_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, sort=sort)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_search** | **str**| Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number | [optional] 
 **filters_created_at** | **datetime**| Return items within a specific created at ISO8601 datetime range | [optional] 
 **filters_updated_at** | **str**| Return items within a specific updated at ISO8601 datetime range | [optional] 
 **filters_standard_cost_code_id** | [**List[int]**](int.md)| Returns vendors associated with the specified standard cost code id(s) | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Returns vendors associated with the specified trade id(s) | [optional] 
 **filters_id** | [**List[int]**](int.md)| Returns vendors with the specified id(s) | [optional] 
 **filters_parent_id** | [**List[int]**](int.md)| Returns vendors with the specified parent id(s) | [optional] 
 **sort** | **str**| Return items with the specified sort | [optional] 

### Return type

[**List[RestV10VendorsGet200ResponseInner]**](RestV10VendorsGet200ResponseInner.md)

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

# **rest_v10_vendors_id_business_register_patch**
> NormalViewBusinessRegister rest_v10_vendors_id_business_register_patch(procore_company_id, id, company_id, business_register_body)

Update Company Vendor Business Register

Update an existing Business Register associated with a specified Vendor.  The Register must already exist.  Changing the identifier of a verified Business Register will set the following attributes to null: verification_status, verified_at

### Example


```python
import procore_sdk
from procore_sdk.models.business_register_body import BusinessRegisterBody
from procore_sdk.models.normal_view_business_register import NormalViewBusinessRegister
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Company Vendor
    company_id = 56 # int | ID of the Company
    business_register_body = procore_sdk.BusinessRegisterBody() # BusinessRegisterBody | 

    try:
        # Update Company Vendor Business Register
        api_response = api_instance.rest_v10_vendors_id_business_register_patch(procore_company_id, id, company_id, business_register_body)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_business_register_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_business_register_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Company Vendor | 
 **company_id** | **int**| ID of the Company | 
 **business_register_body** | [**BusinessRegisterBody**](BusinessRegisterBody.md)|  | 

### Return type

[**NormalViewBusinessRegister**](NormalViewBusinessRegister.md)

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
**404** | Not Found. The Vendor ID was invalid, or the Vendor does not have a Business Register. |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_vendors_id_business_register_post**
> NormalViewBusinessRegister rest_v10_vendors_id_business_register_post(procore_company_id, id, company_id, business_register_body)

Create Company Vendor Business Register

Create a new Business Register associated with a specified Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.business_register_body import BusinessRegisterBody
from procore_sdk.models.normal_view_business_register import NormalViewBusinessRegister
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Company Vendor
    company_id = 56 # int | Unique identifier for the company.
    business_register_body = procore_sdk.BusinessRegisterBody() # BusinessRegisterBody | 

    try:
        # Create Company Vendor Business Register
        api_response = api_instance.rest_v10_vendors_id_business_register_post(procore_company_id, id, company_id, business_register_body)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_business_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_business_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Company Vendor | 
 **company_id** | **int**| Unique identifier for the company. | 
 **business_register_body** | [**BusinessRegisterBody**](BusinessRegisterBody.md)|  | 

### Return type

[**NormalViewBusinessRegister**](NormalViewBusinessRegister.md)

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
**409** | A Business Register is already associated with the Vendor. |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_vendors_id_get**
> RestV10VendorsIdGet200Response rest_v10_vendors_id_get(procore_company_id, id, company_id, view=view, page=page, per_page=per_page)

Show company vendor

Show detail on a specified Company Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_vendors_id_get200_response import RestV10VendorsIdGet200Response
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the vendor
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # Show company vendor
        api_response = api_instance.rest_v10_vendors_id_get(procore_company_id, id, company_id, view=view, page=page, per_page=per_page)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the vendor | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10VendorsIdGet200Response**](RestV10VendorsIdGet200Response.md)

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

# **rest_v10_vendors_id_patch**
> RestV10VendorsGet200ResponseInner rest_v10_vendors_id_patch(procore_company_id, id, company_vendor_body, view=view, run_configurable_validations=run_configurable_validations)

Update company vendor

Update a specified Company Vendor.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.company_vendor_body import CompanyVendorBody
from procore_sdk.models.rest_v10_vendors_get200_response_inner import RestV10VendorsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the vendor
    company_vendor_body = procore_sdk.CompanyVendorBody() # CompanyVendorBody | 
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update company vendor
        api_response = api_instance.rest_v10_vendors_id_patch(procore_company_id, id, company_vendor_body, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the vendor | 
 **company_vendor_body** | [**CompanyVendorBody**](CompanyVendorBody.md)|  | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10VendorsGet200ResponseInner**](RestV10VendorsGet200ResponseInner.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_vendors_post**
> RestV10VendorsGet200ResponseInner rest_v10_vendors_post(procore_company_id, company_vendor_body, view=view, run_configurable_validations=run_configurable_validations)

Create company vendor

Create a new Vendor associated with a specified Company.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.company_vendor_body import CompanyVendorBody
from procore_sdk.models.rest_v10_vendors_get200_response_inner import RestV10VendorsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_vendor_body = procore_sdk.CompanyVendorBody() # CompanyVendorBody | 
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create company vendor
        api_response = api_instance.rest_v10_vendors_post(procore_company_id, company_vendor_body, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_vendor_body** | [**CompanyVendorBody**](CompanyVendorBody.md)|  | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10VendorsGet200ResponseInner**](RestV10VendorsGet200ResponseInner.md)

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

# **rest_v10_vendors_sync_patch**
> RestV10VendorsSyncPatch200Response rest_v10_vendors_sync_patch(procore_company_id, company_vendor_sync_body, run_configurable_validations=run_configurable_validations)

Sync company vendors

Creates or updates a batch of Company Vendors. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.  #### Documentation  The purpose of this API is to allow one or more vendors to be created or updated.  The caller provides an array of hashes, each hash containing the attributes for a single vendor. The attribute names in each hash match those used by the Create and Update Company Vendors APIs. Attributes for a maximum of 1000 vendors may be passed with each call.  The API will always return an HTTP status of 200.  The response body will contain two attributes entities and errors. The attributes for each successfully created or updated vendor will appear in the entities list. The attributes for each vendor will match those returned by the Show Company Vendor API. For each vendor which could not be created or updated, the attributes supplied by the caller will be present in the errors list, along with an additional errors attribute which will provide reasons for the failure.  For each vendor the caller supplies data for, the Sync API uses two different types of unique identifier to determine whether a new vendor is to be created, or an existing vendor is to be updated. The unique identifiers are supplied as the ID and origin_id attributes.  If neither unique identifier is provided, Procore will attempt to create a new vendor. For example the request below will create two new Vendors.  ````json {   \"company_id\": 352361,   \"updates\": [     { \"name\": \"New Vendor 1\" },     { \"name\": \"New Vendor 2\" }   ] } ````  The response to this request lists all attributes for the vendors which have been created.  The ID attribute is the Procore unique identifier for a particular vendor. If the caller already knows the Procore unique identifier for a particular vendor (either through the List Company Vendors API or through the Create Company Vendor API) this value can be passed to indicate which vendor is to be updated. Note that if the caller passes an ID value which Procore does not recognise, Procore will report an error.  The caller does not need to be aware of the unique identifiers assigned by Procore for each vendor in order to create or update them. Instead the caller can provide their own unique identifier for the vendor in the `origin_id` attribute. If Procore cannot find a vendor with the supplied `origin_id` it will create a new one. If Procore can find a vendor with the supplied `origin_id` it will update it.  Note that alongside the origin_id attribute, Procore also provides an `origin_data` attribute. Procore does not interpret the contents of this attribute. The caller can use this to store and retrieve their own contextual information about this vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.company_vendor_sync_body import CompanyVendorSyncBody
from procore_sdk.models.rest_v10_vendors_sync_patch200_response import RestV10VendorsSyncPatch200Response
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_vendor_sync_body = procore_sdk.CompanyVendorSyncBody() # CompanyVendorSyncBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Sync company vendors
        api_response = api_instance.rest_v10_vendors_sync_patch(procore_company_id, company_vendor_sync_body, run_configurable_validations=run_configurable_validations)
        print("The response of CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyVendorsApi->rest_v10_vendors_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_vendor_sync_body** | [**CompanyVendorSyncBody**](CompanyVendorSyncBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10VendorsSyncPatch200Response**](RestV10VendorsSyncPatch200Response.md)

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

