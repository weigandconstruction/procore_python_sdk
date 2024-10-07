# BIMFileExtractionItemError

An error that can occur during model processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error code | [optional] 
**type** | **str** | Error type | [optional] 
**message** | **str** | Human readable error message | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_error import BIMFileExtractionItemError

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemError from a JSON string
bim_file_extraction_item_error_instance = BIMFileExtractionItemError.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemError.to_json())

# convert the object into a dict
bim_file_extraction_item_error_dict = bim_file_extraction_item_error_instance.to_dict()
# create an instance of BIMFileExtractionItemError from a dict
bim_file_extraction_item_error_from_dict = BIMFileExtractionItemError.from_dict(bim_file_extraction_item_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


