# RFQChangeOrderPackages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**title** | **str** | Title | [optional] 
**status** | **str** | Status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_order_packages import RFQChangeOrderPackages

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeOrderPackages from a JSON string
rfq_change_order_packages_instance = RFQChangeOrderPackages.from_json(json)
# print the JSON string representation of the object
print(RFQChangeOrderPackages.to_json())

# convert the object into a dict
rfq_change_order_packages_dict = rfq_change_order_packages_instance.to_dict()
# create an instance of RFQChangeOrderPackages from a dict
rfq_change_order_packages_from_dict = RFQChangeOrderPackages.from_dict(rfq_change_order_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


