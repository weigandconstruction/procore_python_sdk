# RestV10ChangeOrderRequestsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by_id** | **int** | Created by id | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**change_order_package_id** | **int** | Change Order Package ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**revision** | **int** | Revision | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_requests_get200_response_inner import RestV10ChangeOrderRequestsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderRequestsGet200ResponseInner from a JSON string
rest_v10_change_order_requests_get200_response_inner_instance = RestV10ChangeOrderRequestsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderRequestsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_change_order_requests_get200_response_inner_dict = rest_v10_change_order_requests_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChangeOrderRequestsGet200ResponseInner from a dict
rest_v10_change_order_requests_get200_response_inner_from_dict = RestV10ChangeOrderRequestsGet200ResponseInner.from_dict(rest_v10_change_order_requests_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


