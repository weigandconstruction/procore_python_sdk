# RestV10PotentialChangeOrdersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by_id** | **int** | Created by id | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**revision** | **int** | Revision | [optional] 
**change_reason** | **str** | Change reason | [optional] 
**schedule_impact_amount** | **int** | Schedule Impact | [optional] 
**change_order_request_id** | **int** | Change Order Request | [optional] 
**executed** | **bool** | Executed | [optional] [default to False]
**grand_total** | **str** | Total including markup | [optional] 
**change_order_request_title** | **str** | Change Order Request Title | [optional] 
**change_order_package_title** | **str** | Change Order Package Title | [optional] 
**potential_change_order_acronym_number** | **str** | If the change order tier is single tier, an empty string. Otherwise, the PCO acronym and number. | [optional] 
**change_order_request_acronym_number** | **str** | If the change order tier is single tier or two-tiered, an empty string. Otherwise, the COR acronym and change order request number. | [optional] 
**change_order_package_acronym_number** | **str** | The CCO acronym and change order package number. | [optional] 
**change_order_tiers** | **int** | Number of Change Order Tiers | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_potential_change_orders_get200_response_inner import RestV10PotentialChangeOrdersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PotentialChangeOrdersGet200ResponseInner from a JSON string
rest_v10_potential_change_orders_get200_response_inner_instance = RestV10PotentialChangeOrdersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10PotentialChangeOrdersGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_potential_change_orders_get200_response_inner_dict = rest_v10_potential_change_orders_get200_response_inner_instance.to_dict()
# create an instance of RestV10PotentialChangeOrdersGet200ResponseInner from a dict
rest_v10_potential_change_orders_get200_response_inner_from_dict = RestV10PotentialChangeOrdersGet200ResponseInner.from_dict(rest_v10_potential_change_orders_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


