# BIMFileExtractionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_file_extraction_id** | **int** | BIM File extraction ID | [optional] 
**item_type** | **str** | Extraction type | [optional] 
**progress** | **float** | Extraction progress | [optional] 
**artifact** | [**BIMFileExtractionItemArtifact**](BIMFileExtractionItemArtifact.md) |  | [optional] 
**error** | [**BIMFileExtractionItemError**](BIMFileExtractionItemError.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item import BIMFileExtractionItem

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItem from a JSON string
bim_file_extraction_item_instance = BIMFileExtractionItem.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItem.to_json())

# convert the object into a dict
bim_file_extraction_item_dict = bim_file_extraction_item_instance.to_dict()
# create an instance of BIMFileExtractionItem from a dict
bim_file_extraction_item_from_dict = BIMFileExtractionItem.from_dict(bim_file_extraction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


