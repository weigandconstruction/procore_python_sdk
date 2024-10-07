# TimeAndMaterialNotificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_notification** | [**TimeAndMaterialNotification**](TimeAndMaterialNotification.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_notification_body import TimeAndMaterialNotificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialNotificationBody from a JSON string
time_and_material_notification_body_instance = TimeAndMaterialNotificationBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialNotificationBody.to_json())

# convert the object into a dict
time_and_material_notification_body_dict = time_and_material_notification_body_instance.to_dict()
# create an instance of TimeAndMaterialNotificationBody from a dict
time_and_material_notification_body_from_dict = TimeAndMaterialNotificationBody.from_dict(time_and_material_notification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


