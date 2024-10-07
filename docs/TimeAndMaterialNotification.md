# TimeAndMaterialNotification

Time and Material Notification Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation** | **List[int]** |  | [optional] 
**customer_signed** | **List[int]** |  | [optional] 
**company_signed** | **List[int]** |  | [optional] 
**closed** | **List[int]** |  | [optional] 
**group_equipment_totals_by** | **str** | Grouping configurations for T&amp;M Equipment push to Change Management | [optional] 
**notify_dl_on_customer_signed** | **bool** |  | [optional] 
**notify_dl_on_company_signed** | **bool** |  | [optional] 
**notify_dl_on_creation** | **bool** |  | [optional] 
**notify_dl_on_closed** | **bool** |  | [optional] 
**group_labor_totals_by** | **str** | Grouping configurations for T&amp;M Labor push to Change Management | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_notification import TimeAndMaterialNotification

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialNotification from a JSON string
time_and_material_notification_instance = TimeAndMaterialNotification.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialNotification.to_json())

# convert the object into a dict
time_and_material_notification_dict = time_and_material_notification_instance.to_dict()
# create an instance of TimeAndMaterialNotification from a dict
time_and_material_notification_from_dict = TimeAndMaterialNotification.from_dict(time_and_material_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


