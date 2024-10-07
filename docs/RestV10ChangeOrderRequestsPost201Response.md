# RestV10ChangeOrderRequestsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**creator** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**grand_total** | **float** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**position** | **int** | Position | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**revision** | **int** | Revision | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_requests_post201_response import RestV10ChangeOrderRequestsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderRequestsPost201Response from a JSON string
rest_v10_change_order_requests_post201_response_instance = RestV10ChangeOrderRequestsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderRequestsPost201Response.to_json())

# convert the object into a dict
rest_v10_change_order_requests_post201_response_dict = rest_v10_change_order_requests_post201_response_instance.to_dict()
# create an instance of RestV10ChangeOrderRequestsPost201Response from a dict
rest_v10_change_order_requests_post201_response_from_dict = RestV10ChangeOrderRequestsPost201Response.from_dict(rest_v10_change_order_requests_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


