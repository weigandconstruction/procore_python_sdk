# TimeAndMaterialTimecardBulkUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_timecards** | [**List[TimeAndMaterialTimecardProperties]**](TimeAndMaterialTimecardProperties.md) | Array of Time and material timecard objects | 

## Example

```python
from procore_sdk.models.time_and_material_timecard_bulk_update_body import TimeAndMaterialTimecardBulkUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialTimecardBulkUpdateBody from a JSON string
time_and_material_timecard_bulk_update_body_instance = TimeAndMaterialTimecardBulkUpdateBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialTimecardBulkUpdateBody.to_json())

# convert the object into a dict
time_and_material_timecard_bulk_update_body_dict = time_and_material_timecard_bulk_update_body_instance.to_dict()
# create an instance of TimeAndMaterialTimecardBulkUpdateBody from a dict
time_and_material_timecard_bulk_update_body_from_dict = TimeAndMaterialTimecardBulkUpdateBody.from_dict(time_and_material_timecard_bulk_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


