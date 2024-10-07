# BIMFileExtractionItemType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Extraction type | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_type import BIMFileExtractionItemType

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemType from a JSON string
bim_file_extraction_item_type_instance = BIMFileExtractionItemType.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemType.to_json())

# convert the object into a dict
bim_file_extraction_item_type_dict = bim_file_extraction_item_type_instance.to_dict()
# create an instance of BIMFileExtractionItemType from a dict
bim_file_extraction_item_type_from_dict = BIMFileExtractionItemType.from_dict(bim_file_extraction_item_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


