# BIMFileExtractionCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | User Company name | [optional] 
**id** | **int** | Login Information ID | [optional] 
**name** | **str** | User name | [optional] 
**locale** | **str** | User dictionary | [optional] 
**login** | **str** | User email | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_created_by import BIMFileExtractionCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionCreatedBy from a JSON string
bim_file_extraction_created_by_instance = BIMFileExtractionCreatedBy.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionCreatedBy.to_json())

# convert the object into a dict
bim_file_extraction_created_by_dict = bim_file_extraction_created_by_instance.to_dict()
# create an instance of BIMFileExtractionCreatedBy from a dict
bim_file_extraction_created_by_from_dict = BIMFileExtractionCreatedBy.from_dict(bim_file_extraction_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


