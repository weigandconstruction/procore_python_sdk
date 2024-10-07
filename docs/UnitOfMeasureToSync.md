# UnitOfMeasureToSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Unit of Measure | [optional] 
**name** | **str** | Name of the Unit of Measure | [optional] 
**uom_category_id** | **int** | ID of the Unit of Measure Category | [optional] 

## Example

```python
from procore_sdk.models.unit_of_measure_to_sync import UnitOfMeasureToSync

# TODO update the JSON string below
json = "{}"
# create an instance of UnitOfMeasureToSync from a JSON string
unit_of_measure_to_sync_instance = UnitOfMeasureToSync.from_json(json)
# print the JSON string representation of the object
print(UnitOfMeasureToSync.to_json())

# convert the object into a dict
unit_of_measure_to_sync_dict = unit_of_measure_to_sync_instance.to_dict()
# create an instance of UnitOfMeasureToSync from a dict
unit_of_measure_to_sync_from_dict = UnitOfMeasureToSync.from_dict(unit_of_measure_to_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


