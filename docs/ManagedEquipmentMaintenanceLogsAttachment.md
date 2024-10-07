# ManagedEquipmentMaintenanceLogsAttachment

Maintenance Log Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**presentation_url** | **str** | URL | [optional] 
**url** | **str** | URL | [optional] 
**thumbnail_url** | **str** | URL | [optional] 
**filename** | **str** | Filename of Managed Equipment Attachment | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentMaintenanceLogsAttachment from a JSON string
managed_equipment_maintenance_logs_attachment_instance = ManagedEquipmentMaintenanceLogsAttachment.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentMaintenanceLogsAttachment.to_json())

# convert the object into a dict
managed_equipment_maintenance_logs_attachment_dict = managed_equipment_maintenance_logs_attachment_instance.to_dict()
# create an instance of ManagedEquipmentMaintenanceLogsAttachment from a dict
managed_equipment_maintenance_logs_attachment_from_dict = ManagedEquipmentMaintenanceLogsAttachment.from_dict(managed_equipment_maintenance_logs_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


