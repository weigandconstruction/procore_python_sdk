# RFQSpecificationSection

Specification Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_section_id** | **int** | ID | [optional] 
**spec_section_description** | **str** | Description | [optional] 
**spec_section_number** | **str** | Number | [optional] 

## Example

```python
from procore_sdk.models.rfq_specification_section import RFQSpecificationSection

# TODO update the JSON string below
json = "{}"
# create an instance of RFQSpecificationSection from a JSON string
rfq_specification_section_instance = RFQSpecificationSection.from_json(json)
# print the JSON string representation of the object
print(RFQSpecificationSection.to_json())

# convert the object into a dict
rfq_specification_section_dict = rfq_specification_section_instance.to_dict()
# create an instance of RFQSpecificationSection from a dict
rfq_specification_section_from_dict = RFQSpecificationSection.from_dict(rfq_specification_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


