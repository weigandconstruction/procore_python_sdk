# RFQPotentialChangeOrders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Potential change order id | [optional] 
**created_at** | **datetime** | Potential change order created at | [optional] 
**created_by_id** | **int** | Potential change order creator id | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Potential change order due date | [optional] 
**invoiced_date** | **date** | Potential change order invoiced date | [optional] 
**number** | **str** | Potential change order number | [optional] 
**paid_date** | **date** | Potential change order paid date | [optional] 
**reviewed_at** | **datetime** | Potential change order reviewed at | [optional] 
**title** | **str** | Potential change order title | [optional] 
**status** | **str** | Potential change order status | [optional] 
**updated_at** | **datetime** | Potential change order updated at | [optional] 
**change_order_request_id** | **int** | Change Order Request ID | [optional] 
**executed** | **bool** | Executed (or not) | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**revision** | **int** | Revision | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**change_reason** | **str** | Change reason | [optional] 
**change_order_request_title** | **str** | Change Order Request Title | [optional] 
**change_order_package_title** | **str** | Change Order Package Title | [optional] 
**potential_change_order_acronym_number** | **str** | If the change order tier is single tier, an empty string. Otherwise, the PCO acronym and number. | [optional] 
**change_order_request_acronym_number** | **str** | If the change order tier is single tier or two-tiered, an empty string. Otherwise, the COR acronym and change order request number. | [optional] 
**change_order_package_acronym_number** | **str** | The CCO acronym and change order package number. | [optional] 
**change_order_tiers** | **int** | Number of Change Order Tiers | [optional] 

## Example

```python
from procore_sdk.models.rfq_potential_change_orders import RFQPotentialChangeOrders

# TODO update the JSON string below
json = "{}"
# create an instance of RFQPotentialChangeOrders from a JSON string
rfq_potential_change_orders_instance = RFQPotentialChangeOrders.from_json(json)
# print the JSON string representation of the object
print(RFQPotentialChangeOrders.to_json())

# convert the object into a dict
rfq_potential_change_orders_dict = rfq_potential_change_orders_instance.to_dict()
# create an instance of RFQPotentialChangeOrders from a dict
rfq_potential_change_orders_from_dict = RFQPotentialChangeOrders.from_dict(rfq_potential_change_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


