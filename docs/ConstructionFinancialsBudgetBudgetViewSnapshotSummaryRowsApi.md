# procore_sdk.ConstructionFinancialsBudgetBudgetViewSnapshotSummaryRowsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get**](ConstructionFinancialsBudgetBudgetViewSnapshotSummaryRowsApi.md#rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get) | **GET** /rest/v1.0/budget_view_snapshots/{budget_view_snapshot_id}/summary_rows | List Budget View Snapshot Summary Rows


# **rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get**
> List[RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner] rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get(procore_company_id, budget_view_snapshot_id, project_id, page=page, per_page=per_page, biller=biller, cost_code_id=cost_code_id, cost_code_name=cost_code_name, root_cost_code_id=root_cost_code_id, root_cost_code_name=root_cost_code_name, category_id=category_id, budget_line_item_id=budget_line_item_id, group_by=group_by, budget_row_type=budget_row_type)

List Budget View Snapshot Summary Rows

Return a list of all Budget View Snapshot Summary Rows for a project and budget view snapshot. The type of row returned is dependent on the value used in the group_by query param.  Note: In addition to all the fields outlined in the response, there will be an additional key for each visible standard, source, and formula column created for the particular budget view.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get200_response_inner import RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetViewSnapshotSummaryRowsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    budget_view_snapshot_id = 56 # int | Budget View Snapshot ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    biller = ['biller_example'] # List[str] | Return item(s) within a specific biller. Format is biller[]=id=1,type=SubJob or biller[]=id=1,type=Project (optional)
    cost_code_id = [56] # List[int] | Return item(s) within a specific Cost Code id or range of Cost Code IDs (optional)
    cost_code_name = ['cost_code_name_example'] # List[str] | Return item(s) within a specific Cost Code name or range of Cost Code names (optional)
    root_cost_code_id = [56] # List[int] | Return item(s) within a specific Root Cost Code id or range of Root Cost Code IDs (optional)
    root_cost_code_name = ['root_cost_code_name_example'] # List[str] | Return item(s) within a specific Root Cost Code name or range of Root Cost Code names (optional)
    category_id = [56] # List[int] | Return item(s) within a specific category id (line item type id) or range of category IDs (optional)
    budget_line_item_id = [56] # List[int] | Return item(s) within a specific budget line item id or range of budget line item IDs (optional)
    group_by = 'group_by_example' # str | Groups the data. Value can be a comma separated string. Default is biller,root_cost_code (optional)
    budget_row_type = 'budget_row_type_example' # str | Return budgeted, unbudgeted or all item(s) from all budget rows for a project. Default is all. Note that when the unbudgeted or all values are supplied, the subtotals may change depending on the presence of rows that have budgeted false (optional)

    try:
        # List Budget View Snapshot Summary Rows
        api_response = api_instance.rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get(procore_company_id, budget_view_snapshot_id, project_id, page=page, per_page=per_page, biller=biller, cost_code_id=cost_code_id, cost_code_name=cost_code_name, root_cost_code_id=root_cost_code_id, root_cost_code_name=root_cost_code_name, category_id=category_id, budget_line_item_id=budget_line_item_id, group_by=group_by, budget_row_type=budget_row_type)
        print("The response of ConstructionFinancialsBudgetBudgetViewSnapshotSummaryRowsApi->rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetViewSnapshotSummaryRowsApi->rest_v10_budget_view_snapshots_budget_view_snapshot_id_summary_rows_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **budget_view_snapshot_id** | **int**| Budget View Snapshot ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **biller** | [**List[str]**](str.md)| Return item(s) within a specific biller. Format is biller[]&#x3D;id&#x3D;1,type&#x3D;SubJob or biller[]&#x3D;id&#x3D;1,type&#x3D;Project | [optional] 
 **cost_code_id** | [**List[int]**](int.md)| Return item(s) within a specific Cost Code id or range of Cost Code IDs | [optional] 
 **cost_code_name** | [**List[str]**](str.md)| Return item(s) within a specific Cost Code name or range of Cost Code names | [optional] 
 **root_cost_code_id** | [**List[int]**](int.md)| Return item(s) within a specific Root Cost Code id or range of Root Cost Code IDs | [optional] 
 **root_cost_code_name** | [**List[str]**](str.md)| Return item(s) within a specific Root Cost Code name or range of Root Cost Code names | [optional] 
 **category_id** | [**List[int]**](int.md)| Return item(s) within a specific category id (line item type id) or range of category IDs | [optional] 
 **budget_line_item_id** | [**List[int]**](int.md)| Return item(s) within a specific budget line item id or range of budget line item IDs | [optional] 
 **group_by** | **str**| Groups the data. Value can be a comma separated string. Default is biller,root_cost_code | [optional] 
 **budget_row_type** | **str**| Return budgeted, unbudgeted or all item(s) from all budget rows for a project. Default is all. Note that when the unbudgeted or all values are supplied, the subtotals may change depending on the presence of rows that have budgeted false | [optional] 

### Return type

[**List[RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner]**](RestV10BudgetViewSnapshotsBudgetViewSnapshotIdSummaryRowsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

